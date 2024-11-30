"""
Sorted Merge: 
You are given two sorted arrays, A and B, 
where A has a large enough buffer at the end to hold B. 
Write a method to merge B into A in sorted order.
"""

import unittest


def sorted_merge(arr_a: list[int], arr_b: list[int], arr_a_len: int) -> list[int]:

    # arr_a = [3,4,7,10, None, None, None], arr_b = [1,3,5], arr_a_len = 4

    index_a = arr_a_len - 1
    index_b = len(arr_b) - 1
    current_index = len(arr_a) - 1
    while index_b >= 0 and index_a >= 0 and current_index >= 0:

        if arr_b[index_b] > arr_a[index_a]:
            arr_a[current_index] = arr_b[index_b]
            index_b -= 1
        else:
            arr_a[current_index] = arr_a[index_a]
            index_a -= 1

        current_index -= 1

    if index_b < 0:
        # done
        return arr_a

    # index_a is empty
    while current_index >= 0:
        arr_a[current_index] = arr_b[current_index]
        current_index -= 1

    return arr_a


class Test(unittest.TestCase):

    def test_sorted_merge(self):

        a = [3, 4, 7, 10, None, None, None]
        b = [1, 3, 5]

        self.assertEqual(sorted_merge(a, b, 4), [1, 3, 3, 4, 5, 7, 10])


if __name__ == "__main__":
    unittest.main()
