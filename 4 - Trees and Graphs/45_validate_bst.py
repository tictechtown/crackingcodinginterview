'''
Validate BST: 
Implement a function to check if a binary tree is a binary search tree.
'''

# validate:
# BST if 
# node > max(node.left)
# node < min(node.right)

import unittest

from Tree import TreeNode, create_binary_tree


def validate_bst(root:TreeNode|None) -> bool:

    
    def helper(root: TreeNode | None, min:int, max:int):
        if not root:
            return True
        if root.value < min or root.value > max:
            return False
        
        return helper(root.left, min, root.value) and helper(root.right, root.value, max)

    
    return helper(root, float('-inf'), float('inf'))


class Test(unittest.TestCase):

    test = ([5, 4, 7, 2, None, 6, 8, 1,3] , [1, 2, None, 3])

    def test_list_of_depths(self):

        root = create_binary_tree(self.test[0])
        self.assertEqual(validate_bst(root), True)
        root = create_binary_tree(self.test[1])
        self.assertEqual(validate_bst(root), False)


if __name__ == "__main__":
    unittest.main()
