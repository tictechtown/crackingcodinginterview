"""
Palindrome Permutation:
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

Example:
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
"""

import unittest
from collections import defaultdict


# Time: O(N). Space: O(N)
def palindrome_permutation(input: str) -> bool:
    counter = defaultdict(int)
    oddKeyCount = 0
    total_len = 0
    for ch in input.lower():
        if ch.isalnum():
            total_len += 1
            counter[ch] += 1
            if (counter[ch] % 2) == 0:
                oddKeyCount -= 1
            else:
                oddKeyCount += 1

    # Counter represents palindrome iff
    # all keys are even (if string is even)
    # all keys but 1 are even (if string is odd)

    if (total_len % 2) == 0:
        return oddKeyCount == 0
    else:
        return oddKeyCount == 1


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = palindrome_permutation(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
