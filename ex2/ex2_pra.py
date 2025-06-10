from abc import ABC,abstractmethod

import heapq

class search_problem(ABC):
    def start_node(self):
        pass

    def is_goal(self,node):
        pass

    def neighbours(self,node):
        pass
    def heuristic(self,node):
        pass

class Path():
    def __init__(self,node,initial=None,edge=None):
        self.node=node
        self.initial=initial
        self.edge=edge

    def __repr__(self):
        if self.initial:
            return f"{self.initial} -> {self.edge.to_node}"

        return f"{self.node}"

class Edge():
    def __init__(self,from_node,to_node,cost=1):
        self.from_node=from_node
        self.to_node=to_node
        self.cost=cost

class Searchproblemfromexplicitgraph(search_problem):

    def __init__(self,nodes,edges,start,goals,heuristic_dict=None):
        self.nodes=nodes
        self.edges=edges
        self.start=start
        self.goals=goals
        self.heuristic_dict=heuristic_dict or {}


    def start_node(self):
        return self.start

    def is_goal(self,node):
        return node in self.goals
    def neighbours(self,node):
        return [edge for edge in self.edges if edge.from_node==node]
    def heuristic(self,node):
        return self.heuristic_dict.get(node,0)

class FrontierPQ():
    def __init__(self):
        self.elements=[]
        self.frontier_index=0

    def add(self,path,priority):
        heapq.heappush(self.elements,(priority,self.frontier_index,path))
        self.frontier_index+=1
    def pop(self):
        if self.elements:
            return heapq.heappop(self.elements)[-1]
        return None
    def is_empty(self):
        return (len(self.elements)==0)


class Searcher:
    def __init__(self,problem):
        self.problem=problem
        self.frontier=FrontierPQ()
        self.explored=set()

    def search(self):
        startnode=self.problem.start_node()
        path=Path(node=startnode)
        self.frontier.add(path,0)

        while not self.frontier.is_empty():
            path=self.frontier.pop()
            node=path.node

            if self.problem.is_goal(node):
                goals.remove(node)
                return path

            self.explored.add(node)

            for edge in self.problem.neighbours(node):
                if edge.to_node not in self.explored:
                    new_path=Path(edge.to_node,path,edge)
                    total_cost=(path.edge.cost if path.edge else 0)+edge.cost
                    priority=total_cost+self.problem.heuristic(edge.to_node)
                    self.frontier.add(new_path,priority)
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

problem = Searchproblemfromexplicitgraph(nodes, edges, start, goals, heuristics)

searcher = Searcher(problem)

result_path= searcher.search()
print("Result Path:", result_path)



    
