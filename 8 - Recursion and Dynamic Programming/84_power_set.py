"""
Power Set:
Write a method to return all subsets of a set.
"""

import unittest


def power_set(input: list[int]) -> list[list[int]]:
    output = [[]]
    for index in range(len(input)):
        result = output[:]
        for o in output:
            result.append(o + [input[index]])
        output = result

    return output


class Test(unittest.TestCase):
    test = [1, 2, 3]
    result = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    def test_power_set(self):
        self.assertEqual(power_set(self.test), self.result)


if __name__ == "__main__":
    unittest.main()
