"""
List of Depths: 
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
(e.g., if you have a tree with depth D, you'll have D linked lists).
"""

import unittest
from collections import deque

from Tree import TreeNode, create_binary_tree


def create_list(root: TreeNode | None) -> list[list[int]]:
    output = []
    if not root:
        return output

    queue = deque([root])
    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                level.append(node.value)
                queue.append(node.left)
                queue.append(node.right)

        if level:
            output.append(level)

    return output


class Test(unittest.TestCase):

    test = ([1, 4, 5, 4, 3, None, 9, 7, 0, 10], [[1], [4, 5], [4, 3, 9], [7, 0, 10]])

    def test_list_of_depths(self):

        root = create_binary_tree(self.test[0])
        res = create_list(root)
        self.assertEqual(res, self.test[1])


if __name__ == "__main__":
    unittest.main()
