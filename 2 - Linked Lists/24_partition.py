"""
Partition:
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
If x is contained within the list, the values of x only need to be after the elements less than x (see below).
The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

from LinkedList import LinkedList, LinkedListNode
import unittest


# Time: O(N), Space: O(1)
def partition(head: LinkedListNode, value: int) -> LinkedListNode:
    node = head
    dummy_left = LinkedListNode(value=-1)
    dummy_right = LinkedListNode(value=-1)
    left = dummy_left
    right = dummy_right

    while node:
        if node.value < value:
            left.next = node
            left = left.next
        else:
            right.next = node
            right = right.next
        node = node.next

    right.next = None
    left.next = dummy_right.next
    return dummy_left.next


class Test(unittest.TestCase):
    testA = ([3, 5, 8, 5, 10, 2, 1], 5, [3, 2, 1, 5, 8, 5, 10])

    def test(self):
        ll = LinkedList()
        for value in self.testA[0]:
            ll.add(value)

        ll.head = partition(ll.head, self.testA[1])
        self.assertEqual([n.value for n in ll], self.testA[2])


if __name__ == "__main__":
    unittest.main()
