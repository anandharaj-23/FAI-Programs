import heapq

class Puzzle():
    def __init__(self, board, parent=None, move=None, depth=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.zero_index = self.board.index(0)
        
    def __lt__(self, other):
        return self.cost < other.cost

    def generate_children(self):
        children = []
        x, y = divmod(self.zero_index, 3)
        directions = {
            'Up': (x - 1, y),
            'Down': (x + 1, y),
            'Left': (x, y - 1),
            'Right': (x, y + 1)
        }
        
        for move, (new_x, new_y) in directions.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_board = self.board[:]
                new_board[self.zero_index], new_board[new_index] = new_board[new_index], new_board[self.zero_index]
                children.append(Puzzle(new_board, self, move, self.depth + 1))
        
        return children
    
    def get_path(self):
        path = []
        states = []
        current = self
        while current.move:
            path.append(current.move)
            states.append(current.board)
            current = current.parent
        return path[::-1], states[::-1]

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i:i+3])
        print()

def manhattan_heuristic(state, goal):
    distance = 0
    for i in range(1, 9):
        curr_pos = state.board.index(i)
        goal_pos = goal.index(i)
        curr_x, curr_y = divmod(curr_pos, 3)
        goal_x, goal_y = divmod(goal_pos, 3)
        distance += abs(curr_x - goal_x) + abs(curr_y - goal_y)
    return distance

def out_of_sequence_heuristic(state, goal):
    score = 0
    for i in range(8):
        if state.board[i] != goal[i]:
            if i == 4:
                score += 1
            elif state.board[i] != goal[i + 1]:
                score += 2
    return score

def a_star_search(start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    closed_set = set()
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current.board == goal:
            return current.get_path()
        
        closed_set.add(tuple(current.board))
        
        for child in current.generate_children():
            if tuple(child.board) in closed_set:
                continue
            child.cost = child.depth + heuristic(child, goal)
            heapq.heappush(open_set, (child.cost, child))
    
    return None

def greedy_best_first_search(start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    closed_set = set()
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current.board == goal:
            return current.get_path()
        
        closed_set.add(tuple(current.board))
        
        for child in current.generate_children():
            if tuple(child.board) in closed_set:
                continue
            child.cost = heuristic(child, goal)
            if tuple(child.board) not in closed_set:
                heapq.heappush(open_set, (child.cost, child))
                closed_set.add(tuple(child.board))
    
    return None

start_state = [7, 2, 4, 5, 0, 6, 8, 3, 1]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

start_node = Puzzle(start_state)
print("Greedy Best-First Search:")
path, states = greedy_best_first_search(start_node, goal_state, manhattan_heuristic)
if path:
    print("Solution \n")
    for move, state in zip(path, states):
        print(f"Move: {move}")
        state_node = Puzzle(state)
        state_node.print_board()
else:
    print("No solution found")
print()

print("A* Search :")
path, states = a_star_search(start_node, goal_state, out_of_sequence_heuristic)
if path:
    print("Solution\n")
    for move, state in zip(path, states):
        print(f"Move: {move}")
        state_node = Puzzle(state)
        state_node.print_board()
else:
    print("No solution found")
