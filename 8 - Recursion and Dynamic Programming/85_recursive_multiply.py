"""
Recursive Multiply:
Write a recursive function to multiply two positive integers without using the *operator.
You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.
"""

import unittest


def multiply(valueA: int, valueB: int) -> int:
    if valueA == 0 or valueB == 0:
        return 0
    if valueA == 1:
        return valueB
    if valueB == 1:
        return valueA

    return valueA + multiply(valueA, valueB - 1)


class Test(unittest.TestCase):
    test = [(2, 3, 6), (5, 8, 40)]

    def test_multiply(self):
        for [a, b, res] in self.test:
            self.assertEqual(multiply(a, b), res)


if __name__ == "__main__":
    unittest.main()
