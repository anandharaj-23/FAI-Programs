
from abc import ABC, abstractmethod
import heapq

class Search_problem(ABC):
    @abstractmethod
    def start_node(self):
        pass

    @abstractmethod
    def is_goal(self, node):
        pass
    
    @abstractmethod
    def neighbors(self, node):
        pass

    @abstractmethod
    def heuristic(self, node):
        pass

class Path:
    def __init__(self, node, initial=None, edge=None):
        self.node = node
        self.initial = initial
        self.edge = edge

    def __repr__(self):
        if self.initial:
            return f"{self.initial} -> {self.edge.to_node} (cost: {self.edge.cost})"
        return f"{self.node}"

class Edge:
    def __init__(self, from_node, to_node, cost=1):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

    def __repr__(self):
        return f"Edge({self.from_node} -> {self.to_node}, cost: {self.cost})"

class Searchproblemfromexplicitgraph(Search_problem):
    def __init__(self, nodes, edges, start, goals, heuristics=None, title=""):
        self.nodes = nodes
        self.edges = edges
        self.start = start
        self.goals = goals
        self.title = title
        self.heuristics = heuristics or {}

    def start_node(self):
        return self.start

    def is_goal(self, node):
        return node in self.goals

    def neighbors(self, node):
        return [edge for edge in self.edges if edge.from_node == node]

    def heuristic(self, node):
        return self.heuristics.get(node, 0)

    def __repr__(self):
        return f"SearchProblem(title: {self.title}, start: {self.start}, goals: {self.goals}, nodes: {self.nodes})"

class FrontierPQ:
    def __init__(self):
        self.elements = []
        self.frontier_index = 0

    def add(self, path, priority):
        heapq.heappush(self.elements, (priority, self.frontier_index, path))
        self.frontier_index += 1

    def pop(self):
        if self.elements:
            return heapq.heappop(self.elements)[-1]
        return None

    def is_empty(self):
        return len(self.elements) == 0

class Searcher:
    def __init__(self, problem):
        self.problem = problem
        self.frontier = FrontierPQ()
        self.explored = set()
        

    def search(self):
        start_node = self.problem.start_node()
        start_path = Path(node=start_node)
        self.frontier.add(start_path, 0)

        while not self.frontier.is_empty():
            path = self.frontier.pop()
            node = path.node

            if self.problem.is_goal(node):
                goals.remove(node)
                return path

            self.explored.add(node)

            for edge in self.problem.neighbors(node):
                if edge.to_node not in self.explored:
                    new_path = Path(node=edge.to_node, initial=path, edge=edge)
                    total_cost = (path.edge.cost if path.edge else 0) + edge.cost
                    priority = total_cost + self.problem.heuristic(edge.to_node)
                    self.frontier.add(new_path, priority)
                    
        return None

nodes = {'A','B','C','D','E'}
    
edges = [
    Edge('A', 'B', 1),
    Edge('A', 'C', 3),
    Edge('B', 'C', 2),
    Edge('B', 'E', 5),
    Edge('C', 'D', 4),
    Edge('C', 'E', 2)
]
start = 'A'
goals = {'E'}

heuristics = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 0
}

problem = Searchproblemfromexplicitgraph(nodes, edges, start, goals, heuristics, title="A* Algorithm")

searcher = Searcher(problem)

result_path= searcher.search()
print("Result Path:", result_path)


