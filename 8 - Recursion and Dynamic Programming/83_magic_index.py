"""
Magic Index:
A magic index in an array A[ 0••• n -1] is defined to be an index such that A[ i] = i.
Given a sorted array of distinct integers,
write a method to find a magic index, if one exists, in array A.
"""

import unittest


# Input: [-5, -3, 0, 3, 10, 20]
# Output: 3

# Brute force:
# for i in range(n): if arr[i] == i: return i
# O(N)

# Better -> O(logN)


def find_magic_index(arr: list[int]) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid

        if arr[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1

    return None


class Test(unittest.TestCase):
    test = [-5, -3, 0, 3, 10, 20]

    def test_list_of_depths(self):
        index = find_magic_index(self.test)
        self.assertEqual(index, 3)


if __name__ == "__main__":
    unittest.main()
