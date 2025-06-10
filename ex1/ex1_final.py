from abc import ABC, abstractmethod

class SearchProblem(ABC):
    def start_node(self):
        pass

    def is_goal(self, node):
        pass

    def neighbors(self, node):
        pass

    def heuristic(self, node):
        pass


class Path:
    def __init__(self, node, initial=None, edge=None):
        self.node = node
        self.initial = initial
        self.edge = edge

    def __repr__(self):
        if self.initial:
            return f"{self.initial} -> {self.node}"
        return self.node

    def nodes(self):
        # Return all nodes in this path as a list
        if self.initial:
            return self.initial.nodes() + [self.node]
        return [self.node]

    def contains(self, node):
        return node in self.nodes()


class Edge:
    def __init__(self, from_node, to_node, cost=1):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost


class SearchProblemWithExplicitGraph(SearchProblem):
    def __init__(self, nodes, edges, start, goals, heuristic_dict=None):
        self.nodes = nodes
        self.edges = edges
        self.start = start
        self.goals = goals
        self.heuristic_dict = heuristic_dict or {}

    def start_node(self):
        return self.start

    def is_goal(self, node):
        return node in self.goals

    def neighbors(self, node):
        return [edge for edge in self.edges if edge.from_node == node]

    def heuristic(self, node):
        return self.heuristic_dict.get(node, 0)


class Searcher:
    def __init__(self, problem):
        self.problem = problem
        self.frontier = [Path(problem.start_node())]  # Stack-based approach for DFS

    def search(self):
        while self.frontier:
            path = self.frontier.pop()  # LIFO stack for DFS
            node = path.node

            if self.problem.is_goal(node):
                return path

            for edge in self.problem.neighbors(node):
                if not path.contains(edge.to_node):  # Avoid revisiting nodes in the current path
                    new_path = Path(edge.to_node, path, edge)
                    self.frontier.append(new_path)

        return None


# Test with predefined start and goal
problem1 = SearchProblemWithExplicitGraph(
    {'A', 'B', 'C', 'D', 'G'},
    [
        Edge('A', 'B', 3),
        Edge('A', 'C', 1),
        Edge('B', 'D', 1),
        Edge('B', 'G', 3),
        Edge('C', 'B', 1),
        Edge('C', 'D', 3),
        Edge('D', 'G', 1)
    ],
    start='A',
    goals={'G'},
    heuristic_dict={}
)

searcher = Searcher(problem1)
print("\nSolution: ")
print(f"All possible paths from 'A' to 'G'\n")

loop = True
while loop:
    solution = searcher.search()
    if solution is None:
        loop = False
    else:
        print(solution)
