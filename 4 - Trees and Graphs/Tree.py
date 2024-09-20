class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def traverse_in_order(self, acc):

        if self.left:
            self.left.traverse_in_order(acc)
        acc.append(self.value)
        if self.right:
            self.right.traverse_in_order(acc)


class TreeNodeWithParent:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def traverse_in_order(self, acc):

        if self.left:
            self.left.traverse_in_order(acc)
        acc.append(self.value)
        if self.right:
            self.right.traverse_in_order(acc)



def create_binary_tree(input: list[int | None]) -> TreeNode | None:
    if not input:
        return None
    nodes = [TreeNode(input[i]) if input[i] is not None else None  for i in range(len(input))]
    
    index = 0
    while index < len(input) // 2:
        if nodes[index]:
            nodes[index].left = nodes[2*index+1] if (2*index+1) < len(input) else None
            nodes[index].right = nodes[2*index+2] if (2*index+2) < len(input) else None
        index += 1
    return nodes[0]

def create_binary_tree_with_parent(input: list[int | None]) -> TreeNodeWithParent | None:
    if not input:
        return None
    nodes = [TreeNodeWithParent(input[i]) if input[i] is not None else None  for i in range(len(input))]
    
    index = 0
    while index < len(input) // 2:
        if nodes[index]:
            nodes[index].left = nodes[2*index+1] if (2*index+1) < len(input) else None
            nodes[index].right = nodes[2*index+2] if (2*index+2) < len(input) else None
            if nodes[index].left:
                nodes[index].left.parent = nodes[index]
            if nodes[index].right:
                nodes[index].right.parent = nodes[index]
        index += 1
    return nodes[0]