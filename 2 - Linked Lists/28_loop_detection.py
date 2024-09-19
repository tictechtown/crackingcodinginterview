"""
Loop Detection:
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
"""

from LinkedList import LinkedListNode, LinkedList
import unittest


# Time: O(N), Space: O(1)
def detect_loop(head: LinkedListNode) -> int:
    fast = head
    slow = head
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next

        if fast == slow:
            break

    slow = head
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return slow.value


class Test(unittest.TestCase):
    testA = ([3, 4, 2, 0, 8], 2)

    def test(self):
        llA = LinkedList()
        for value in self.testA[0]:
            llA.add(value)

        llA.tail.next = llA.head.next.next
        self.assertEqual(detect_loop(head=llA.head), self.testA[1])


if __name__ == "__main__":
    unittest.main()
