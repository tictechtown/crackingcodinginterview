"""
Sort Stack: 
Write a program to sort a stack such that the smallest items are on the top. 
You can use an additional temporary stack, but you may not copy the elements into any other data structure

The stack supports the following operations: push, pop, peek, and isEmpty
"""

import unittest

# input [1,3,2,4,5,2,6,4]
# tmp [4]
# tmp [4, 6]
# tmp [4,6,2] -> [2,4,6]

# tmp [4,6]
# val: 2
# stack: [1,3,2,4,5,6,4]
# tmp []
# tmp [2]
# tmp [2, 4, 6]


def sort_stack(stack: list[int]):

    tmp_stack = []
    while len(stack):  # not isEmpty

        val = stack.pop()
        if len(tmp_stack) == 0:  # isEmpty
            tmp_stack.append(val)
        else:
            count = 0
            while tmp_stack and tmp_stack[-1] > val:  # peek
                stack.append(tmp_stack.pop())
                count += 1
            tmp_stack.append(val)
            for _ in range(count):
                tmp_stack.append(stack.pop())

    # now, tmp_stack is sorted from smallest to biggest
    while tmp_stack:
        stack.append(tmp_stack.pop())

    return stack


class Test(unittest.TestCase):

    test = ([1, 3, 2, 4, 5, 2, 6, 4], [6, 5, 4, 4, 3, 2, 2, 1])

    def test_stack(self):
        self.assertEqual(sort_stack(self.test[0]), self.test[1])


if __name__ == "__main__":
    unittest.main()
