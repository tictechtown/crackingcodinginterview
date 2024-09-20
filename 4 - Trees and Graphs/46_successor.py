'''
Successor: 
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. 
You may assume that each node has a link to its parent.
'''

import unittest

from Tree import TreeNodeWithParent, create_binary_tree_with_parent


def find_next_node(node: TreeNodeWithParent | None):

    if not node:
        return None
    

    if node.right:
        runner = node.right
        while runner.left:
            runner = runner.left
        return runner
    else:
        return node.parent



class Test(unittest.TestCase):

    test = ([5, 4, 7, 2, None, 6, 8, 1,3] , [1, 2, None, 3])

    def test_successor(self):

        root = create_binary_tree_with_parent(self.test[0])
        self.assertEqual(find_next_node(root).value, 6)
        self.assertEqual(find_next_node(root.left).value, 5)
        self.assertEqual(find_next_node(root.left.left).value, 3)


if __name__ == "__main__":
    unittest.main()
