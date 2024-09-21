"""
Robot in a Grid:
Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them.
Design an algorithm to find a path for the robot from the top left to the bottom right.
"""

import unittest


# 0 -> can move
# 1 -> off-limit
def find_path(grid: list[list[int]]) -> list[tuple[int, int]] | None:
    m = len(grid)
    n = len(grid[0])

    path = []

    def dfs(rowIndex, colIndex, path):
        if rowIndex == m - 1 and colIndex == n - 1:
            # found our path
            path.append((rowIndex, colIndex))
            return path

        if grid[rowIndex][colIndex] == 1:
            # off limit
            return None

        path += [(rowIndex, colIndex)]

        if rowIndex + 1 < m:
            if dfs(rowIndex + 1, colIndex, path):
                return path
        if colIndex + 1 < n:
            if dfs(rowIndex, colIndex + 1, path):
                return path

        return None

    dfs(0, 0, path)
    return path


class Test(unittest.TestCase):
    test = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]

    def test_list_of_depths(self):
        path = find_path(self.test)
        self.assertEqual(
            path, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3)]
        )


if __name__ == "__main__":
    unittest.main()
