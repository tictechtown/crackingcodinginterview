"""
Return Kth to Last:
Implement an algorithm to find the kth to last element of a singly linked list.
"""

from LinkedList import LinkedList, LinkedListNode
import unittest


# Time: O(N), Space: O(1)
def return_kth_to_last(head: LinkedListNode, k: int) -> int:
    runner = head
    while k:
        runner = runner.next
        k -= 1

    node = head
    while runner:
        runner = runner.next
        if runner:
            node = node.next

    return node.value


class Test(unittest.TestCase):
    testA = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 7)

    def test(self):
        ll = LinkedList()
        for value in self.testA[0]:
            ll.add(value)

        output = return_kth_to_last(ll.head, self.testA[1])
        self.assertEqual(output, self.testA[2])


if __name__ == "__main__":
    unittest.main()
