'''
Check Subtree: 
T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. 
That is, if you cut off the tree at node n, the two trees would be identical.
'''

from Tree import TreeNode

# TODO


def check_subtree(rootA:TreeNode | None, rootB: TreeNode|None) -> bool:

    if not rootA and not rootB:
        return True
    
    if not rootA or not rootB:
        return False
    
    if rootA.value != rootB.value:
        return check_subtree(rootA.left, rootB) or check_subtree(rootA.right, rootB)

    return check_identical(rootA, rootB)


def check_identical(rootA:TreeNode | None, rootB: TreeNode|None) -> bool:
    if not rootA and not rootB:
        return True
    
    if not rootA or not rootB:
        return False
    if rootA.value != rootB.value:
        return False
    return check_identical(rootA.left, rootB.left) and check_identical(rootA.right, rootB.right)


