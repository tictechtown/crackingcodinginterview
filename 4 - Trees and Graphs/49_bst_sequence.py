'''
BST Sequences: 
A binary search tree was created by traversing through an array from left to right and inserting each element. 
Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
'''
# TODO

import unittest

from Tree import TreeNode

'''
    4
2       5
  3

  
[4]
bst_sequence(2)
    bst_sequence(3)
bst_sequence(5)
  

  
'''



def bst_sequence(root:TreeNode | None) -> list[list[int]]:

    result = []
    if not root:
        result.append([])
        return result

    prefix = []
    prefix.append(root.value)

    left_seq = bst_sequence(root.left)
    right_seq = bst_sequence(root.right)

    for l_seq in left_seq:
        for r_seq in right_seq:
            output = []
            weave_list(l_seq, r_seq, output, prefix)
            for o in output:
                result.append(o)
    
    return result

def weave_list(left:list[list[int]], right:list[list[int]], output :list[list[int]], prefix:list[int]):
    if not left or not right:
        res = prefix[:]
        for seq in (left or right):
            res.append(seq)
        output.append(res)
        return
    
    
    prefix.append(left.pop(0))
    weave_list(left, right, output, prefix)
    left.insert(0, prefix.pop())

    prefix.append(right.pop(0))
    weave_list(left, right, output, prefix)
    right.insert(0, prefix.pop())

class Test(unittest.TestCase):

    test = (
        ["a", "b", "c", "d", "e", "f"],
        [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")],
        ["e", "f", "b", "a", "d", "c"],
    )

    def test_bst_sequence(self):

        self.assertEqual(bst_sequence(self.test[0], self.test[1]), self.test[2])


if __name__ == "__main__":
    unittest.main()
