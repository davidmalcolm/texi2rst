# A minimal IR for transforming texinfo XML into rst
import unittest

class Node:
    def __repr__(self):
        return 'Node()'

    def dump(self, f_out, depth=0):
        f_out.write('%s%r\n' %  (' ' * depth, self))

    def is_element(self, kind):
        if isinstance(self, Element):
            if self.kind == kind:
                return True

    def iter_depth_first(self):
        yield self
        if isinstance(self, Element):
            for child in self.children:
                for item in child.iter_depth_first():
                    yield item

    def iter_depth_first_edges(self):
        if isinstance(self, Element):
            for child in self.children:
                yield (self, child)
                for src, dst in child.iter_depth_first_edges():
                    yield (src, dst)

    def to_dom_node(self, dom_doc):
        if isinstance(self, Element):
            dom_node = dom_doc.createElement(self.kind)
            for k, v in self.attrs.iteritems():
                dom_node.setAttribute(k, v)
            for child in self.children:
                dom_node.appendChild(child.to_dom_node(dom_doc))
            return dom_node
        elif isinstance(self, Comment):
            return dom_doc.createComment(self.data)
        else:
            assert isinstance(self, Text)
            return dom_doc.createTextNode(self.data)

class Element(Node):
    def __init__(self, kind, attrs=None):
        self.kind = kind
        if attrs:
            self.attrs = attrs
        else:
            self.attrs = {}
        self.children = []
        self.rst_kind = None

    def __repr__(self):
        return 'Element(%r, %r, %r)' % (self.kind, self.attrs, self.rst_kind)

    def dump(self, f_out, depth=0):
        f_out.write('%s%r\n' %  (' ' * depth, self))
        for child in self.children:
            child.dump(f_out, depth + 1)

    def first_element_named(self, name):
        for child in self.children:
            if isinstance(child, Element):
                if child.kind == name:
                    return child

    def get_sole_text(self):
        if len(self.children) == 1:
            child = self.children[0]
            if isinstance(child, Text):
                return child

    def get_first_text(self):
        for child in self.children:
            if isinstance(child, Text):
                return child

    def get_all_text(self):
        result = ''
        for child in self.children:
            if isinstance(child, Text):
                result += child.data
            elif isinstance(child, Element):
                result += child.get_all_text()
        return result

    def delete_children_named(self, name):
        new_children = []
        for child in self.children:
            if child.is_element(name):
                continue
            new_children.append(child)
        self.children = new_children

    def add_element(self, kind, **kwargs):
        new_child = Element(kind, kwargs)
        self.children.append(new_child)
        return new_child

    def add_comment(self, data):
        self.children.append(Comment(data))

    def add_text(self, data):
        if self.children:
            last_child = self.children[-1]
            if isinstance(last_child, Text):
                last_child.data += data
                return
        self.children.append(Text(data))

    def to_dom_doc(self):
        from xml.dom.minidom import getDOMImplementation
        impl = getDOMImplementation()
        dom_doc = impl.createDocument(None, self.kind, None)
        top_element = dom_doc.documentElement
        for child in self.children:
            top_element.appendChild(child.to_dom_node(dom_doc))
        return dom_doc

class Comment(Node):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return 'Comment(%r)' % self.data

class Text(Node):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return 'Text(%r)' % self.data

class NodeTests(unittest.TestCase):
    def test_node_to_dom(self):
        a = Element('A')
        b = Element('B')
        c = Element('C')
        a.children = [b, Text('foo'), c]
        b.children = [Text('within b'),
                      Comment('ignore'),
                      Text('also within b')]

        xmldom = a.to_dom_doc()
        xmlstr = xmldom.toprettyxml(indent='  ')
        self.assertEqual(xmlstr,
                         ('''<?xml version="1.0" ?>
<A>
  <B>
    within b
    <!--ignore-->
    also within b
  </B>
  foo
  <C/>
</A>
'''))

if __name__ == '__main__':
    unittest.main()
