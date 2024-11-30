"""
Sparse Search: 
Given a sorted array of strings that is interspersed with empty strings, 
write a method to find the location of a given string.
"""

import unittest


def sparse_search(input: list[str], target: int) -> int:

    left = 0
    right = len(input) - 1
    while left <= right:
        middle = (left + right) // 2
        value = input[middle]

        if value == "":
            # found the nearest middle
            pos = 1
            while True:

                if 0 > (middle - pos) and (middle + pos) >= len(input):
                    return -1  # out of the array

                if 0 <= (middle - pos) and input[middle - pos] != "":
                    middle = middle - pos
                    value = input[middle]
                    break
                if (middle + pos) < len(input) and input[middle + pos] != "":
                    middle = middle + pos
                    value = input[middle]
                    break

        if value == target:
            return middle

        if target < value:
            right = middle - 1
        else:
            left = middle + 1

    # not found
    return -1


class Test(unittest.TestCase):

    def test_sorted_merge(self):

        a = ["a", "", "", "", "b", "c", "", "", "d", "", ""]
        self.assertEqual(sparse_search(a, "d"), 8)


if __name__ == "__main__":
    unittest.main()
