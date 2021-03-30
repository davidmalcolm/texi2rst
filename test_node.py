#!/usr/bin/env python3

from node import *
import unittest

class NodeTests(unittest.TestCase):
    def make_tree(self):
        a = Element('A')
        b = Element('B')
        c = Element('C')
        a.children = [b, Text('foo'), c]
        b.children = [Text('within b'),
                      Comment('ignore'),
                      Text('also within b')]
        return a

    def test_node_to_dom(self):
        a = self.make_tree()
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

    def test_node_to_xmlstr(self):
        a = self.make_tree()
        xmlstr = a.toxml()
        self.assertMultiLineEqual(
            xmlstr,
            '<A><B>within b<!--ignore-->also within b</B>foo<C/></A>')

    def test_header(self):
        a = Element('A')
        xmlstr = a.toxml(dtd_line='<!DOCTYPE texinfo PUBLIC "-//GNU//DTD TexinfoML V5.0//EN" "http://www.gnu.org/software/texinfo/dtd/5.0/texinfo.dtd">')
        self.assertMultiLineEqual(
            xmlstr,
            '''<?xml version="1.0"?>
<!DOCTYPE texinfo PUBLIC "-//GNU//DTD TexinfoML V5.0//EN" "http://www.gnu.org/software/texinfo/dtd/5.0/texinfo.dtd">
<A/>''')
