'''
First Common Ancestor
'''

'''
FCA(nodeA, nodeB)


FCA


'''


def find_fca(root, nodeA, nodeB):

    if not root:
        return None

    if root == nodeA:
        return nodeA
    if root == nodeB:
        return nodeB
    
    left = find_fca(root.left, nodeA, nodeB)
    right = find_fca(root.right, nodeA, nodeB)

    if left and right:
        return root
    
    return left or right


