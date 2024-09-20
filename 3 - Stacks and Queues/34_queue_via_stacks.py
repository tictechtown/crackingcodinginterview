"""
Queue via Stacks: 
Implement a MyQueue class which implements a queue using two stacks.
"""

import unittest


class MyQueue:
    # FIFO

    def __init__(self):

        self.stackA = []
        self.stackB = []

    def push(self, item: int):
        self.stackA.append(item)

    def peek(self):

        if not len(self.stackA):
            raise ValueError

        while self.stackA:
            self.stackB.append(self.stackA.pop())

        val = self.stackB[-1]
        while self.stackB:
            self.stackA.append(self.stackB.pop())
        return val

    def pop(self):
        if not len(self.stackA):
            raise ValueError

        while self.stackA:
            self.stackB.append(self.stackA.pop())

        val = self.stackB.pop()
        while self.stackB:
            self.stackA.append(self.stackB.pop())

        return val


class Test(unittest.TestCase):

    # push, min, pop, push, min
    test = [1, 2, 3, 4, 5]

    def test_stack(self):

        queue = MyQueue()

        for i in range(len(self.test)):
            queue.push(self.test[i])

        for i in range(len(self.test)):
            self.assertEqual(queue.pop(), self.test[i])


if __name__ == "__main__":
    unittest.main()
