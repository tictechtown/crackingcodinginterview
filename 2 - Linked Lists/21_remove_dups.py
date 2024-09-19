"""
Remove Dups:
Write code to remove duplicates from an unsorted linked list.
"""

from LinkedList import LinkedList, LinkedListNode
import unittest


# Time: O(N), Space: O(N)
def remove_duplicate(head: LinkedListNode) -> LinkedListNode:
    seen_values = set()

    node = head

    dummy = LinkedListNode(value=-1)
    runner = dummy

    while node:
        if node.value not in seen_values:
            seen_values.add(node.value)
            runner.next = node
            runner = runner.next
        node = node.next

    runner.next = None

    return dummy.next


"""
Remove Dups:
How would you solve this problem if a temporary buffer is not allowed?
"""


# 1, 4, 2, 4, 3, 4, 7, 7, 7, 5, 1, 2, 6, 7
# 1


# Time: O(N2), Space: O(1)
def remove_duplicate_no_buffer(head: LinkedListNode) -> LinkedListNode:
    if head is None:
        return

    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head


class Test(unittest.TestCase):
    testA = ([1, 4, 2, 4, 3, 4, 7, 7, 7, 5, 1, 2, 6, 7], [1, 4, 2, 3, 7, 5, 6])

    def test_remove_duplicate(self):
        ll = LinkedList()
        for value in self.testA[0]:
            ll.add(value)

        ll.head = remove_duplicate(ll.head)
        self.assertEqual([node.value for node in ll], self.testA[1])

    def test_remove_duplicate_no_buffer(self):
        ll = LinkedList()
        for value in self.testA[0]:
            ll.add(value)

        ll.head = remove_duplicate_no_buffer(ll.head)
        self.assertEqual([node.value for node in ll], self.testA[1])


if __name__ == "__main__":
    unittest.main()
