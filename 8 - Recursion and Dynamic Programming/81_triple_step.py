"""
Triple Step:
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""

import unittest

# n = 0
# -> way: 1

# n = 1
# -> way: 1

# n = 2:
# -> way: 2 (1+1 or 2+0)

# n= 3:
# -> way: 4 (1+1+1, 2+1, 1+2, 3+0)


def count_run_up(steps: int) -> int:  # 2
    memo = [0] * (steps + 1)  # 5
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2

    for step in range(3, steps + 1):
        memo[step] = memo[step - 1] + memo[step - 2] + memo[step - 3]

    return memo[-1]


class Test(unittest.TestCase):
    test = [(3, 4), (2, 2)]

    def test_list_of_depths(self):
        for [steps, count] in self.test:
            self.assertEqual(count_run_up(steps), count)


if __name__ == "__main__":
    unittest.main()
