from abc import ABC,abstractmethod

class Edge:
    def __init__(self,from_node,to_node,cost=0):
        self.from_node=from_node
        self.to_node=to_node
        self.cost=cost
    def __repr__(self):
        return f" (From node) {self.from_node} -> (to node) {self.to_node} (cost) {self.cost}"

class Path:
    def __init__(self,initial,edge=None):
        self.initial=initial
        self.edge=edge

    def end(self):
        if self.edge is None:
            return self.initial
        else:
            return self.edge.to_node

    def __repr__(self):
        if self.edge is None:
            return f"{self.initial}"

        else:
            return f"{self.initial} -> {self.edge.to_node}"

class SearchProblemWithExplicitGraph:
    def __init__(self,title,nodes,edges,start,goals,heuristic_dict=None):
        self.title = title
        self.nodes = nodes
        self.edges = edges
        self.start = start
        self.goals = goals
        self.heuristic_dict = heuristic_dict if heuristic_dict is not None else {}

    def start_node(self):
        return self.start
    
    def is_goal(self,node):
        return node in self.goals

    def neighbors(self,node):
        return [edge for edge in self.edges if edge.from_node==node]

    def heuristic(self,node):
        return self.heuristic.get(node,0)

class Searcher:

    def __init__(self,problem):
        self.problem=problem
        self.frontier=[Path(problem.start_node())]

    def search(self):

        while self.frontier:
            path=self.frontier.pop()
            node=path.end()

            if self.problem.is_goal(node):
                return path

            for edge in self.problem.neighbors(node):
                new_path=Path(path,edge)
                self.frontier.append(new_path)
        return None

start_v=input("Enter the starting vertex:")
goal_v=input("Enter the goal vertex:")

problem1 = SearchProblemWithExplicitGraph(
    'Problem 1',
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
    start=start_v,
    goals=goal_v
)

loop=True
searcher = Searcher(problem1)
print("\nSolution: ")
print(f"All possible paths from {start_v} to {goal_v}\n")
while loop is True:
    solution = searcher.search()
    if solution is None:
        loop=False
    else:
        print(solution)








    




    
