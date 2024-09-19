"""
One Away:
There are three types of edits that can be performed on strings:
- insert a character,
- remove a character,
- or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

import unittest


# Time: O(N). Space: O(1)
def is_one_away(input: str, matching: str) -> bool:
    if len(input) == len(matching):
        # check character_replaced_count
        return _character_replaced_count(input, matching) <= 1
    elif len(input) == len(matching) + 1:
        # check character_added
        return _character_added_count(input, matching) <= 1
    elif len(matching) == len(input) + 1:
        # check character_added
        return _character_added_count(matching, input) <= 1
    return False


def _character_replaced_count(input: str, matching: str) -> int:
    count = 0
    for i in range(len(input)):
        if input[i] != matching[i]:
            count += 1
    return count


def _character_added_count(input: str, matching: str) -> int:
    # input is > than matching
    count = 0
    rightIndex = 0
    for i in range(len(input)):
        if rightIndex < len(matching) and input[i] == matching[rightIndex]:
            rightIndex += 1
        else:
            count += 1
    return count


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("paleabc", "pleabc", True),
        ("pale", "ble", False),
        ("a", "b", True),
        ("", "d", True),
        ("d", "de", True),
        ("pale", "pale", True),
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
        ("pale", "pse", False),
        ("ples", "pales", True),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pale", "pkle", True),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = is_one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
