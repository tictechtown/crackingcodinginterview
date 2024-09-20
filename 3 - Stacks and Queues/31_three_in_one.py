"""
Three in One: 
Describe how you could use a single array to implement three stacks.
"""

import unittest


class ArrayStack:

    numstacks = 3

    def __init__(self, stack_capacity):
        self.array = [0] * (stack_capacity * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stack_capacity = stack_capacity

    def push(self, stack_index: int, item: int):
        if self._is_full(stack_index):
            raise Exception(f"Cant push. Stack {stack_index} is full")
        self.sizes[stack_index] += 1
        self.array[self._top_index(stack_index)] = item

    def pop(self, stack_index: int):
        if self._is_empty(stack_index):
            raise Exception(f"Cant pop. Stack {stack_index} is empty")

        val = self.array[self._top_index(stack_index)]
        self.sizes[stack_index] -= 1
        return val

    def peek(self, stack_index: int):
        if self._is_empty(stack_index):
            raise Exception(f"Cant pop. Stack {stack_index} is empty")
        return self.array[self._top_index(stack_index)]

    def _is_full(self, stack_index: int):
        return self.sizes[stack_index] == self.stack_capacity

    def _is_empty(self, stack_index: int):
        return self.sizes[stack_index] == 0

    def _top_index(self, stack_index: int):
        return stack_index * self.stack_capacity + self.sizes[stack_index] - 1


class Test(unittest.TestCase):

    def test_stack(self):

        stack = ArrayStack(2)
        for i in range(3):
            with self.assertRaises(Exception):
                stack.pop(i)
            stack.push(i, 3)
            stack.push(i, 5)

        self.assertEqual(stack.peek(1), 5)
        self.assertEqual(stack.pop(1), 5)
        self.assertEqual(stack.peek(1), 3)
        self.assertEqual(stack.peek(2), 5)


if __name__ == "__main__":
    unittest.main()
