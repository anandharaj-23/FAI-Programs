import random

def heuristic(state):
    n=len(state)
    attacks=0

    for i in range(n):
        for j in range(i+1,n):
            if(state[i]==state[j] or abs(state[i]-state[j])==abs(i-j)):
                attacks+=1
    return attacks

def generate_initial_state(n):
        return [random.randint(0,n-1) for _ in range(n)]

def get_neighbors(state):
    neighbors=[]
    n=len(state)

    for col in range(n):
        for row in range(n):
            if row !=state[col]:
                neighbor=state[:]
                neighbor[col]=row
                neighbors.append(neighbor)

    return neighbors

def hill_climbing(n,max_attempts=100):
    attempt=0

    while attempt<max_attempts:
        current_state=generate_initial_state(n)
        print("The initial placement of the queens in each column ",current_state)
        current_cost=heuristic(current_state)

        while True:
            neighbors=get_neighbors(current_state)
            if not neighbors:
                break
            neighbors_costs=[(neighbor,heuristic(neighbor)) for neighbor in neighbors]
            neighbors_costs.sort(key=lambda x:x[1])

            best_neighbor,best_cost=neighbors_costs[0]

            if(best_cost>=current_cost):
                break

            current_state=best_neighbor
            current_cost=best_cost

            if(current_cost==0):
                return current_state

        attempt+=1
    return None

def print_board(state):
    n=len(state)

    board=[['.' for i in range(n)] for j in range(n)]

    for col in range(n):
        board[col][state[col]]='Q'

    for row in board:
        print(' '.join(row))


n=int(input("Enter the value of n:"))
soln=hill_climbing(n)

if(soln):
    print("Solution found:")
    print_board(soln)

else:
    print("Solution Not Found")        


