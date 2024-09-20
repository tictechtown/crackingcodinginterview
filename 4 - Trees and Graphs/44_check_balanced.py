"""
Check Balanced: Implement a function to check if a binary tree is balanced. 
For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
"""

import unittest

from Tree import TreeNode, create_binary_tree


def check_balanced(root: TreeNode | None) -> bool:

    def check_balanced_helper(root: TreeNode | None):
        if not root:
            return (True, 0)

        (leftCond, left) = check_balanced_helper(root.left)
        (rightCond, right) = check_balanced_helper(root.right)

        if not leftCond or not rightCond:
            return (False, 0)

        return (abs(left - right) <= 1, max(left, right) + 1)

    return check_balanced_helper(root)[0]


class Test(unittest.TestCase):

    test = ([1, 4, 5, 4, 3, None, 9, 7, 0, 10], [1, 2, None, 3])

    def test_list_of_depths(self):

        root = create_binary_tree(self.test[0])
        self.assertEqual(check_balanced(root), True)
        root = create_binary_tree(self.test[1])
        self.assertEqual(check_balanced(root), False)


if __name__ == "__main__":
    unittest.main()
