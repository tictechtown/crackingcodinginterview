"""
Check Permutation:
Given two strings,
write a method to decide if one is a permutation of the other.
"""

import unittest
from collections import Counter


# Time: O(N). Space: O(N)
def check_permutation(inputA: str, inputB: str) -> bool:
    counterA = Counter(inputA)
    counterB = Counter(inputB)

    return counterA == counterB


class Test(unittest.TestCase):
    dataT = (
        ("abcd", "bacd"),
        ("3563476", "7334566"),
        ("wef34f", "wffe34"),
    )
    dataF = (
        ("abcd", "d2cba"),
        ("2354", "1234"),
        ("dcw4f", "dcw5f"),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
