"""
Stack Min: 
How would you design a stack which, 
in addition to push and pop, 
has a function min which returns the minimum element? 
Push, pop and min should all operate in 0(1) time.
"""

import unittest


class StackMin:

    def __init__(self):
        self.stack = []

    def push(self, value):
        if len(self.stack) == 0 or value < self.min():
            self.stack.append((value, value))
        else:
            self.stack.append((value, self.min()))

    def peek(self, value):
        return self.stack[-1][0]

    def pop(self):
        (value, minValue) = self.stack.pop()
        return value

    def min(self):
        return self.stack[-1][1]


class Test(unittest.TestCase):

    # push, min, pop, push, min
    test = ([4, 3, 6, 0, 0, 2, 1, 2, 3, 4, 5], [4, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0], 3, 3)

    def test_stack(self):

        stack = StackMin()

        for i in range(len(self.test[0])):
            stack.push(self.test[0][i])
            self.assertEqual(stack.min(), self.test[1][i])
        while len(stack.stack) > self.test[2]:
            stack.pop()
        self.assertEqual(stack.min(), self.test[2])


if __name__ == "__main__":
    unittest.main()
