"""
Search in Rotated Array: 
Given a sorted array of n integers that has been rotated an unknown number of times, 
write code to find an element in the array. 
You may assume that the array was originally sorted in increasing order.
"""

import unittest


def search_in_rotated_array(rotated_arr: list[int], target: int) -> int:

    left = 0
    right = len(rotated_arr) - 1

    while left <= right: # l: 0 r:8 -> l:
        middle = (left + right) // 2

        if rotated_arr[middle] == target:
            return middle

        if rotated_arr[left] <= rotated_arr[middle]:
            # left part is not rotated:
            if rotated_arr[left] <= target < rotated_arr[middle]:
                # search in [left, middle]
                right = middle - 1
            else:
                # search in [middle, right]
                left = middle + 1
        else:
            # right part is not rotated
            if rotated_arr[right] >= target > rotated_arr[middle]:
                # search in [middle, right]
                left = middle + 1
            else:
                right = middle - 1

    # not found
    return -1


class Test(unittest.TestCase):

    def test_sorted_merge(self):

        a = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        self.assertEqual(search_in_rotated_array(a, 5), 1)
        self.assertEqual(search_in_rotated_array(a, 1), 6)
        self.assertEqual(search_in_rotated_array(a, 0), -1)


if __name__ == "__main__":
    unittest.main()
