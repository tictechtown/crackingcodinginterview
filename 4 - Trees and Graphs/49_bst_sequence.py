'''
BST Sequences: 
A binary search tree was created by traversing through an array from left to right and inserting each element. 
Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
'''
# TODO

from Tree import TreeNode


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
    
    
    prefix.append(left.pop(0))
    weave_list(left, right, output, prefix)
    left.insert(0, prefix.pop())

    prefix.append(right.pop(0))
    weave_list(left, right, output, prefix)
    right.insert(0, prefix.pop())