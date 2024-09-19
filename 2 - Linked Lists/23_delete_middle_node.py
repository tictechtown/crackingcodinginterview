"""
Delete Middle Node:
Implement an algorithm to delete a node in the middle
(i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list,
given only access to that node.
"""

from LinkedList import LinkedList, LinkedListNode
import unittest


# Time: O(N), Space: O(1)
def delete_middle_node(head: LinkedListNode):
    fast = head
    slow = head
    while fast:
        fast = fast.next
        if not fast.next:
            slow.next = slow.next.next

        if fast:
            fast = fast.next
            slow = slow.next

    return head


class Test(unittest.TestCase):
    testA = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def test(self):
        ll = LinkedList()
        for value in self.testA[0]:
            ll.add(value)

        ll.head = delete_middle_node(ll.head)
        self.assertEqual([n.value for n in ll], self.testA[1])


if __name__ == "__main__":
    unittest.main()
