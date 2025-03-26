import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.NORMAL, "http://example.com")
        node4 = TextNode("This is a code text node", TextType.CODE)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)        
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node2, node4)
        
if __name__ == '__main__':
    unittest.main()