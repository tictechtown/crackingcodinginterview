"""
Sum Lists:
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1 's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
"""

from LinkedList import LinkedListNode, LinkedList
import unittest


# Time: O(N), Space: O(N), N:MAX(A,B)
def sum_list(headA: LinkedListNode, headB: LinkedListNode) -> LinkedListNode:
    dummy = LinkedListNode(value=-1)
    node = dummy
    carry = 0
    while headA or headB or carry:
        value = (headA.value if headA else 0) + (headB.value if headB else 0) + carry
        node.next = LinkedListNode(value % 10)
        node = node.next
        carry = value // 10

        if headA:
            headA = headA.next
        if headB:
            headB = headB.next
    return dummy.next


class Test(unittest.TestCase):
    # 80,243 + 999,984 = 1,080,227
    testA = ([3, 4, 2, 0, 8], [4, 8, 9, 9, 9, 9], [7, 2, 2, 0, 8, 0, 1])

    def test(self):
        llA = LinkedList()
        for value in self.testA[0]:
            llA.add(value)

        llB = LinkedList()
        for value in self.testA[1]:
            llB.add(value)

        llRes = LinkedList()

        llRes.head = sum_list(llA.head, llB.head)
        self.assertEqual([n.value for n in llRes], self.testA[2])


if __name__ == "__main__":
    unittest.main()
