from abc import ABC,abstractmethod

import heapq

class FrontierPQ:

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
        return len(self.element)==0

class Searcher:
    def __init__(self,problem):
        self.problem=problem
        self.frontier=FrontierPQ
        self.explored=set()
    
    def search(self):

        start_node=self.problem.start_node()
        start_path=Path(start=start_node)
        self.frontier.add(start_path,0)

        while not self.frontier.is_empty():
            path=self.frontier.pop()
            node=path.node

            if self.problem.is_goal(node):
                goals.remove(node)
                return path

            self.explored.add(node)
            for edge in self.problem.neighbors(node):
                if edge.to_node not in self.explored:
                    new_path=Path(node=edge.to_node,initial=path,edge=edge)
                    total_cost=(path.edge.cost if path.edge else 0) +edge.cost
                    priority=total_cost+self.problem.heuristic(edge.to_node)
                    self.frontier.add(new_path,priority)
        return None
