"""
Group Anagrams: 
Write a method to sort an array of strings so that all the anagrams are next to each other.
"""

import unittest
from collections import defaultdict


# O(N(K+KLog(K) + O(NLog(N)))
def group_anagrams(input: list[str]) -> list[str]:

    keys = [(sorted(value.lower()), value) for value in input]
    return [values[1] for values in sorted(keys)]


# this is actually a modification of the bucket sort
def group_anagrams_opt(input: list[str]) -> list[str]:

    mapping = defaultdict(list)
    for value in input:
        key = "".join(sorted(value.lower()))
        mapping[key].append(value)

    output = []
    for key in mapping:
        for value in mapping[key]:
            output.append(value)

    return output


class Test(unittest.TestCase):

    def test_sorted_merge(self):

        a = ["abc", "cdb", "awere", "cat", "bac", "tac", "print"]
        b = ["abc", "bac", "cat", "tac", "awere", "cdb", "print"]
        b_opt = ["abc", "bac", "cdb", "awere", "cat", "tac", "print"]
        self.assertEqual(group_anagrams(a), b)
        self.assertEqual(group_anagrams_opt(a), b_opt)


if __name__ == "__main__":
    unittest.main()
