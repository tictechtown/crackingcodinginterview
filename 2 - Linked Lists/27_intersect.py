"""
Intersection:
Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node.
Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
"""

from LinkedList import LinkedListNode, LinkedList
import unittest


def check_intersection(headA: LinkedListNode, headB: LinkedListNode) -> LinkedListNode:
    lenA = _get_len(headA)
    lenB = _get_len(headB)

    if lenA == lenB:
        return headA if headA == headB else None

    if lenB > lenA:
        (headA, headB) = (headB, headA)
        (lenA, lenB) = (lenB, lenA)

    # headA > headB
    while lenA > lenB:
        headA = headA.next
        lenA -= 1

    return headA if headA == headB else None


def _get_len(headA: LinkedListNode) -> int:
    count = 0
    while headA:
        headA = headA.next
        count += 1
    return count


class Test(unittest.TestCase):
    testA = ([3, 4, 2, 0, 8], [4, 8, 9, 9, 9, 9], [8, 4, 8, 9, 9, 9, 9])

    def test(self):
        llA = LinkedList()
        for value in self.testA[0]:
            llA.add(value)

        llB = LinkedList()
        llB.head = llA.tail
        llB.tail = llA.tail
        for value in self.testA[1]:
            llB.add(value)

        llRes = LinkedList()

        llRes.head = check_intersection(llA.head, llB.head)
        self.assertEqual([n.value for n in llRes], self.testA[2])


if __name__ == "__main__":
    unittest.main()
