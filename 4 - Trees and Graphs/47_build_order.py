"""
Build Order: 
You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). 
All of a project's dependencies must be built before the project is. 
Find a build order that will allow the projects to be built. 
If there is no valid build order, return an error.
"""

import unittest
from collections import defaultdict, deque


def find_build_order(
    projects: list[str], dependencies: list[tuple[str, str]]
) -> list[str] | None:
    pass

    in_deg = defaultdict(int)
    adj_list = defaultdict(list)
    for first, second in dependencies:
        in_deg[second] += 1
        adj_list[first].append(second)

    queue = deque([item for item in projects if in_deg.get(item, 0) == 0])
    if not queue:
        return None

    visited = set()
    output = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            output.append(node)

            for neighbor in adj_list.get(node, []):
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    queue.append(neighbor)

    if len(visited) != len(projects):
        return None
    return output


class Test(unittest.TestCase):

    test = (
        ["a", "b", "c", "d", "e", "f"],
        [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")],
        ["e", "f", "b", "a", "d", "c"],
    )

    def test_successor(self):

        self.assertEqual(find_build_order(self.test[0], self.test[1]), self.test[2])


if __name__ == "__main__":
    unittest.main()
