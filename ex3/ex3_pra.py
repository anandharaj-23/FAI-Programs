from collections import deque


class Decantation:

    def __init__(self):
        self.initial_state=(8,0,0)

    def is_goal(self,state):
        return 4 in state

    def next_states(self,state):

        x,y,z=state
        next_state=[]

        transfer=min(x,5-y)

        next_state.append((x-transfer,y+transfer,z))

        transfer=min(x,3-z)

        next_state.append((x-transfer,y,z+transfer))

        transfer=min(y,8-x)

        next_state.append((x+transfer,y-transfer,z))

        transfer=min(y,3-z)
        next_state.append((x,y-transfer,z+transfer))

        transfer=min(z,8-x)

        next_state.append((x+transfer,y,z-transfer))

        transfer=min(z,5-y)

        next_state.append((x,y+transfer,z-transfer))

        return next_state

    def bfs(self):
        frontier=deque([self.initial_state])
        explored={self.initial_state:None}

        while frontier:
            current_state=frontier.popleft()

            print(f"(Exploring {current_state} In the queue : ({list(frontier)})")

            if self.is_goal(current_state):
                return self.construct_path(explored,current_state)

            for state in self.next_states(current_state):
                if state not in explored:
                    frontier.append(state)
                    explored[state]=current_state

    def construct_path(self,explored,state):
        ans=[]

        while state:
            ans.append(state)
            state=explored[state]
        return ans[::-1]

    def print_solution(self):
        soln=self.bfs()

        if soln:

            for state in soln:
                print(state)
        else:
            print("No solution Found\n")

decan=Decantation()
decan.print_solution()






