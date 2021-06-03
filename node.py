#!/usr/bin/env python3

# A minimal IR for transforming texinfo XML into rst
import re
from collections import OrderedDict


class Node:
    def __repr__(self):
        return 'Node()'

    def dump(self, f_out, depth=0):
        f_out.write('%s%r\n' % (' ' * depth, self))

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

    def toxml(self, dtd_line=None):
        """
        XML printer, preserving attribute ordering
        (minidom appears to sort the attribute names
        https://hg.python.org/cpython/file/2.7/Lib/xml/dom/minidom.py#l800)
        """
        def escape(data):
            data = data.replace('&', '&amp;')
            # data = data.replace('"', '&quot;')
            data = data.replace('>', '&gt;')
            data = data.replace('<', '&lt;')
            return data

        if isinstance(self, Element):
            if dtd_line:
                result = '<?xml version="1.0"?>\n'
                result += '%s\n' % dtd_line
            else:
                result = ''
            result += '<%s' % self.kind
            for k, v in self.attrs.items():
                result += ' %s="%s"' % (k, v)
            if self.children:
                result += '>'
                for child in self.children:
                    result += child.toxml()
                result += '</%s>' % self.kind
            else:
                result += '/>'
            return result
        elif isinstance(self, Comment):
            return '<!--%s-->' % self.data
        elif isinstance(self, Entity):
            return '&%s;' % self.name
        else:
            assert isinstance(self, Text)
            return escape(self.data)

    def to_dom_node(self, dom_doc):
        if isinstance(self, Element):
            dom_node = dom_doc.createElement(self.kind)
            for k, v in self.attrs.items():
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
        if not re.match('[a-zA-Z0-9-_]+', kind):
            raise ValueError('bad name for element: %r' % kind)
        self.kind = kind
        if attrs:
            self.attrs = OrderedDict(attrs)
        else:
            self.attrs = OrderedDict()
        self.children = []
        self.rst_kind = None

    def __repr__(self):
        return 'Element(%r, %r, %r)' % (self.kind, self.attrs, self.rst_kind)

    def dump(self, f_out, depth=0):
        f_out.write('%s%r\n' % (' ' * depth, self))
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

    def collapse_to_text(self):
        self.children = [Text(self.get_all_text())]

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

    def prepend_text(self, data):
        if self.children:
            first_child = self.children[0]
            if isinstance(first_child, Text):
                first_child.data = data + first_child.data
                return
        self.children.insert(0, Text(data))

    def add_entity(self, name):
        self.children.append(Entity(name))

    def to_dom_doc(self):
        from xml.dom.minidom import getDOMImplementation
        impl = getDOMImplementation()
        dom_doc = impl.createDocument(None, self.kind, None)
        top_element = dom_doc.documentElement
        for child in self.children:
            top_element.appendChild(child.to_dom_node(dom_doc))
        return dom_doc

    def get_all_elements(self, name):
        result = []
        for child in self.children:
            if isinstance(child, Element):
                if child.kind == name:
                    result.append(child)
                result += child.get_all_elements(name)
        return result


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


class Entity(Node):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Entity(%r)' % self.name


# Visitor base class
class Visitor:
    def visit(self, node, parents=()):
        if isinstance(node, Element):
            early_exit = self.previsit_element(node, parents)
            if early_exit:
                return
            newparents = parents + (node,)
            for child in list(node.children):
                self.visit(child, newparents)
            self.postvisit_element(node, parents)
        elif isinstance(node, Comment):
            self.visit_comment(node)
        elif isinstance(node, Text):
            self.visit_text(node)
        elif isinstance(node, Entity):
            self.visit_entity(node)
        else:
            raise ValueError('unknown node: %r' % (node, ))

    def previsit_element(self, element, parents):
        raise NotImplementedError

    def postvisit_element(self, element, parents):
        raise NotImplementedError

    def visit_comment(self, comment):
        raise NotImplementedError

    def visit_text(self, text):
        raise NotImplementedError

    def visit_entity(self, entity):
        raise NotImplementedError


class NoopVisitor(Visitor):
    def previsit_element(self, element, parents):
        pass

    def postvisit_element(self, element, parents):
        pass

    def visit_comment(self, comment):
        pass

    def visit_text(self, text):
        pass

    def visit_entity(self, entity):
        pass
