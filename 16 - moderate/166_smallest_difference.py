"""
Smallest Difference: 
Given two arrays of integers, 
compute the pair of values (one value in each array) 
with the smallest (non-negative) difference. 

Return the difference.
"""

"""
EXAMPLE
Input: {1, 3, 15, 11, 2}, {23, 127,235, 19, 8} 
Output: 3. 
That is, the pair (11, 8).
"""

import unittest


def smallest_differences(listA: list[int], listB: list[int]) -> tuple[int, int]:

    listA.sort()
    listB.sort()

    indexA = 0
    indexB = 0

    min_diff = abs(listA[indexA] - listB[indexB])

    while indexA < len(listA) and indexB < len(listB):

        if listA[indexA] == listB[indexB]:
            return (indexA, indexB)

        diff = abs(listA[indexA] - listB[indexB])
        min_diff = min(diff, min_diff)

        if listA[indexA] <= listB[indexB]:
            indexA += 1
        else:
            indexB += 1

    return min_diff


class Test(unittest.TestCase):

    def test_sorted_merge(self):

        self.assertEqual(
            smallest_differences([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]), 3
        )


if __name__ == "__main__":
    unittest.main()
