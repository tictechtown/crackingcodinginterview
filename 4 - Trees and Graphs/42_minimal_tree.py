"""
Minimal Tree: 
Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height.
"""

import unittest

from Tree import TreeNode


def create_bst(input: list[int]) -> TreeNode:

    return _create_bst_helper(input, 0, len(input) - 1)


def _create_bst_helper(input: list[int], left: int, right: int) -> TreeNode | None:

    if left > right:
        return None
    if left == right:
        return TreeNode(input[left])

    middle = (left + right) // 2
    node = TreeNode(input[middle])
    node.left = _create_bst_helper(input, left, middle - 1)
    node.right = _create_bst_helper(input, middle + 1, right)
    return node


class Test(unittest.TestCase):

    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_min_tree(self):

        tree = create_bst(self.test)
        res = []
        tree.traverse_in_order(res)
        self.assertEqual(res, self.test)


if __name__ == "__main__":
    unittest.main()
