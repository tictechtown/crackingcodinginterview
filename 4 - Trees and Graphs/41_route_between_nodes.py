"""
Route Between Nodes: 
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""

import unittest
from collections import deque

from Graph import Graph, Node


def has_route(source: Node, target: Node) -> bool:

    queue = deque([source])
    visited = set()
    while queue:

        node = queue.popleft()
        if node == target:
            return True

        if node not in visited:
            visited.add(node)
            for neighbor in node.getAdjacent():
                queue.append(neighbor)

    return False


class Test(unittest.TestCase):

    def test_bfs(self):

        g = Graph()

        nodes = [Node(chr(i + ord("a"))) for i in range(10)]

        nodes[0].addAdjacent(nodes[1])
        nodes[0].addAdjacent(nodes[2])
        nodes[0].addAdjacent(nodes[3])
        nodes[3].addAdjacent(nodes[4])
        nodes[4].addAdjacent(nodes[5])

        for node in nodes:
            g.addNode(node)

        self.assertEqual(has_route(nodes[0], nodes[5]), True)
        self.assertEqual(has_route(nodes[2], nodes[1]), False)

    def test_bfs_with_loop(self):
        g = Graph()

        nodes = [Node(chr(i + ord("a"))) for i in range(10)]

        nodes[0].addAdjacent(nodes[1])
        nodes[1].addAdjacent(nodes[2])
        nodes[2].addAdjacent(nodes[3])
        nodes[3].addAdjacent(nodes[4])
        nodes[4].addAdjacent(nodes[5])
        nodes[4].addAdjacent(nodes[1])

        for node in nodes:
            g.addNode(node)

        self.assertEqual(has_route(nodes[0], nodes[5]), True)


if __name__ == "__main__":
    unittest.main()
