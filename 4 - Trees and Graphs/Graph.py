class Node:

    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacentList = []

    def addAdjacent(self, node):
        self.adjacentList.append(node)

    def getAdjacent(self):
        return self.adjacentList

    def getVertex(self):
        return self.vertex

class Graph:

    def __init__(self):
        self.vertices = []

    def addNode(self, node: Node):
        self.vertices.append(node)

    def getNodes(self):
        return self.vertices
