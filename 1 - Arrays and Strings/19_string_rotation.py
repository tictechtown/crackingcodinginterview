"""
String Rotation:
Assume you have a method isSubstring, which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1
using only one call to isSubstring
(e.g.,"waterbottle" is a rotation of"erbottlewat").
"""

import unittest


# Time: O(N) Space: O(N)
def is_rotation(s1: str, s2: str) -> bool:
    # concatenate s1 twice, s2 should be somewhere in the middle of this new string
    return len(s2) == len(s1) and s2 in (s1 + s1)


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = is_rotation(s1, s2)
            self.assertEqual(actual, expected, f"{s1}, {s2}")


if __name__ == "__main__":
    unittest.main()
