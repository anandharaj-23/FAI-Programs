from collections import deque

class JarsProblem:
    def __init__(self):
        # Start with (8-litre jar, 5-litre jar, 3-litre jar)
        self.start_state = (8, 0, 0)

    def check_goal(self, current):
        """Determine if any jar holds exactly 4 liters."""
        return 4 in current

    def generate_next_states(self, current):
        """Produce all valid successor states from the current state."""
        jar1, jar2, jar3 = current
        next_states = []

        # Transfer from 8-litre to 5-litre
        pour = min(jar1, 5 - jar2)
        next_states.append((jar1 - pour, jar2 + pour, jar3))

        # Transfer from 8-litre to 3-litre
        pour = min(jar1, 3 - jar3)
        next_states.append((jar1 - pour, jar2, jar3 + pour))

        # Transfer from 5-litre to 8-litre
        pour = min(jar2, 8 - jar1)
        next_states.append((jar1 + pour, jar2 - pour, jar3))

        # Transfer from 5-litre to 3-litre
        pour = min(jar2, 3 - jar3)
        next_states.append((jar1, jar2 - pour, jar3 + pour))

        # Transfer from 3-litre to 8-litre
        pour = min(jar3, 8 - jar1)
        next_states.append((jar1 + pour, jar2, jar3 - pour))

        # Transfer from 3-litre to 5-litre
        pour = min(jar3, 5 - jar2)
        next_states.append((jar1, jar2 + pour, jar3 - pour))

        return next_states

    def search_bfs(self):
        """Perform a BFS to find the sequence leading to the goal."""
        queue = deque([self.start_state])
        parent_map = {self.start_state: None}  # Track the path

        while queue:
            state = queue.popleft()
            print(f"Current: {state}, Queue: {list(queue)}")

            if self.check_goal(state):
                return self.trace_path(parent_map, state)

            for next_state in self.generate_next_states(state):
                if next_state not in parent_map:
                    queue.append(next_state)
                    parent_map[next_state] = state

        return None

    def trace_path(self, parent_map, goal_state):
        """Reconstruct the path from start to the goal state."""
        path = []
        while goal_state:
            path.insert(0, goal_state)
            goal_state = parent_map[goal_state]
        return path

    def display_solution(self):
        """Show the steps to reach the goal."""
        solution = self.search_bfs()
        if solution:
            print("Path to solution:")
            for step in solution:
                print(step)
        else:
            print("No valid solution.")

# Execute
problem = JarsProblem()
problem.display_solution()
