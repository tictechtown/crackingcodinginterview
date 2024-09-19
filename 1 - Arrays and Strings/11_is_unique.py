"""
Is Unique:
Implement an algorithm to determine if a string has all unique characters.
"""

import unittest


# time: O(N), space: O(N)
def is_unique(input: str) -> bool:
    uniq_characters = set()
    for ch in input:
        if ch in uniq_characters:
            return False
        uniq_characters.add(ch)
    return True


"""
What if you cannot use additional data structures?
"""


# time: O(N^2), space: O(1)
def is_unique_no_ds(input: str) -> bool:
    for index in range(len(input)):
        for replacingIndex in range(index + 1, len(input)):
            if (
                input[replacingIndex] == input[index]
            ):  # we already seen this character before
                return False

    return True


class Test(unittest.TestCase):
    dataT = [("abcdefghijklmn"), ("S3fheLnaA"), ("")]
    dataF = [("23ds2"), ("hb 627jh=j ()")]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

    def test_unique_no_ds(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique_no_ds(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique_no_ds(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
