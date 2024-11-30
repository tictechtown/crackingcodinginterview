'''
RankfromStream:
Imagine you are reading inastreamofintegers.
Periodically, you wish to be able to look up the rank of a number x 
(the number of values less than or equal tox). 
Implement the data structures and algorithms to support these operations. 
That is, implement the method track (int x), which is called when each number is generated, 
and the method getRankOfNumber(int x), 
which returns the number of values less than or equal to x (not includingx itself).
'''

class Ranker:

    def __init__(self):

        self.stack = []
        self.mapping = {}
    
    def track(self, value:int):
        tmp = []
        while self.stack and self.stack[-1] > value:
            tmp.append(self.stack.pop())
        
        self.mapping[value] = len(self.stack)
        self.stack.append(value)

        while tmp:
            val = tmp.pop()
            self.mapping[val] += 1
            tmp.append(val)
    
    def get_rank_of_number(self, value:int):
        return self.mapping[value] if value in self.mapping else -1
    

# use BST!!

class RankNode:

    def __init__(self, value:int):
        self.value = value
        self.left = None
        self.right = None
        self.left_count = 0 


class BSTRanker:

    def __init__(self) -> None:
        self.root = None
    
    def track(self, value:int):

        if not self.root:
            self.root = RankNode(value)
        else:

            node = self.root
            parent = None
            while node:
                parent = node
                if value < node.value:
                    node = node.left
                    parent.left_count += 1
                else:
                    node = node.right
            if value < parent.value:
                parent.left = RankNode(value)
            else:
                parent.right = RankNode(value)
    
    def get_rank(self, value:int) -> int:
        return self._traverse(self.root, value)
    
    def _traverse(self, node, target):

        if not node:
            return -1
        
        if node.value == target:
            return node.left_count
        
        if target < node.value:
            return self._traverse(node.left, target)
        else:
            right_count = self._traverse(node.right, target)
            if right_count != -1:
                return right_count + node.left_count + 1
            return -1
