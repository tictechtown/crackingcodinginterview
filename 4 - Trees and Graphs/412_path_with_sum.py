"""
Paths with Sum: 
You are given a binary tree in which each node contains an integer value 
(which might be positive or negative). 
Design an algorithm to count the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, 
but it must go downwards (traveling only from parent nodes to child nodes).
"""

import unittest

from Tree import TreeNode, create_binary_tree


def path_with_sum(root: TreeNode | None, target: int) -> int:

    count = 0

    def helper(root, target):
        nonlocal count

        if not root:
            return

        if root.value == target:
            count += 1

        helper(root.left, target - root.value)
        helper(root.right, target - root.value)

    helper(root, target)
    return count


class Test(unittest.TestCase):

    test = ([1, 4, 5, -4, 3, None, 9, 7, 0, 10], 1, 3) # tree, target: 1, count: 3

    def test_path_sum(self):

        root = create_binary_tree(self.test[0])
        self.assertEqual(path_with_sum(root, self.test[1]), self.test[2])


if __name__ == "__main__":
    unittest.main()
