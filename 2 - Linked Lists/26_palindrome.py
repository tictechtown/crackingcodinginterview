from LinkedList import LinkedList, LinkedListNode
import unittest


# Time: O(N), Space: O(N)
def is_palindrome(head: LinkedListNode) -> bool:
    fast = head
    slow = head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True


class Test(unittest.TestCase):
    testA = ([1, 2, 3, 2, 1], True)

    def test(self):
        llA = LinkedList()
        for value in self.testA[0]:
            llA.add(value)

        self.assertEqual(is_palindrome(llA.head), self.testA[1])


if __name__ == "__main__":
    unittest.main()
