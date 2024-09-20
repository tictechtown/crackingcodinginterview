'''
Random Node:
You are implementing a binary tree class from scratch which,
in addition to insert, find, and delete, 
has a method getRandomNode() which returns a random node from the tree. 
All nodes should be equally likely to be chosen.

Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.
'''
import random

# TODO



class RandomNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        

    def insert(self, value):

        if not self.left:
            self.left = RandomNode(value)
        elif not self.right:
            self.right = RandomNode(value)
        else:
            if value <= self.value:
                self.left.insert(value)
            else:
                self.right.insert(value)
    
    def findNode(self, value):

        if self.value == value:
            return self
        
        left,right = None, None
        if self.left:
            left = self.left.findNode(value)
        if self.right:
            right = self.right.findNode(value)
        
        return left or right

class RandomTree:

    def __init__(self) -> None:
        self.root = None
        self.count = 0
    
    def insert(self, value):
        if not self.root:
            self.root = RandomNode(value)
        else:
            self.root.insert(value)
        self.count += 1
    
    def findNode(self, value) -> RandomNode | None:

        if not self.root:
            return None
        
        return self.root.findNode(value)

    def getRandomNode(self) -> RandomNode:
        node_int = random.randint(0, self.count-1)
