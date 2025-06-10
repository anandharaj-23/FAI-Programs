from collections import deque

class Decantation:
    def __init__(self):
        self.initial_state = (8, 0, 0)

    def is_goal(self, state):
        return 4 in state

    def next_states(self, state):
        x, y, z = state
        successors = []

        # Pour from 8-litre to 5-litre
        transfer = min(x, 5 - y)
        successors.append((x - transfer, y + transfer, z))

        # Pour from 8-litre to 3-litre
        transfer = min(x, 3 - z)
        successors.append((x - transfer, y, z + transfer))

        # Pour from 5-litre to 8-litre
        transfer = min(y, 8 - x)
        successors.append((x + transfer, y - transfer, z))

        # Pour from 5-litre to 3-litre
        transfer = min(y, 3 - z)
        successors.append((x, y - transfer, z + transfer))

        # Pour from 3-litre to 8-litre
        transfer = min(z, 8 - x)
        successors.append((x + transfer, y, z - transfer))

        # Pour from 3-litre to 5-litre
        transfer = min(z, 5 - y)
        successors.append((x, y + transfer, z - transfer))

        return successors

    def bfs(self):
        frontier = deque([self.initial_state])
        explored = {self.initial_state: None}  

        while frontier:
            current_state = frontier.popleft()
            print(f"Exploring State: {current_state}, In the Queue: {list(frontier)}")

            if self.is_goal(current_state):
                return self.construct_path(explored, current_state)

            for state in self.next_states(current_state):
                if state not in explored:
                    frontier.append(state)
                    explored[state] = current_state

        return None

    def construct_path(self, explored, state):
        path = []
        while state:
            path.append(state)
            state = explored[state]
        return path[::-1]

    def print_solution(self):
        solution_path = self.bfs()
        if solution_path:
            print("Solution:")
            for state in solution_path:
                print(state)
        else:
            print("No solution exists\n")

problem = Decantation()
problem.print_solution()
