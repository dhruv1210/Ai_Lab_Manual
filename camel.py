#camel.py

total_bananas = int(input("No. Of bananas at start : "))
distance = int(input("Distance to be covered  : "))
load_capacity = int(input("Maximum No. of bananas camel can carry at a time : "))

bananas_lost = 0
start = total_bananas
for i in range(distance) :
    while start > 0 :
        start = start-load_capacity
        if start == 1 :
            bananas_lost = bananas_lost-1
        bananas_lost = bananas_lost+2
    bananas_lost = bananas_lost-1
    start = total_bananas - bananas_lost
    if start == 0:
        break
print("Total bananas delivered : ", start )





#Water Jug Problem

def water_jug_problem(jug1_cap, jug2_cap, target_amount):
    # Initialize the jugs and the possible actions
    j1 = 0
    j2 = 0
    actions = [("fill", 1), ("fill", 2), ("empty", 1), ("empty", 2), ("pour", 1, 2), ("pour", 2, 1)]
    # Create an empty set to store visited states
    visited = set()
    # Create a queue to store states to visit
    queue = [(j1, j2, [])]
    while queue:
        # Dequeue the front state from the queue
        j1, j2, seq = queue.pop(0)
        # If this state has not been visited before, mark it as visited
        if (j1, j2) not in visited:
            visited.add((j1, j2))
            # If this state matches the target amount, return the sequence of actions taken to get to this state
            if j1 == target_amount:
                return seq
            # Generate all possible next states from this state
            for action in actions:
                if action[0] == "fill":
                    if action[1] == 1:
                        next_state = (jug1_cap, j2)
                    else:
                        next_state = (j1, jug2_cap)
                elif action[0] == "empty":
                    if action[1] == 1:
                        next_state = (0, j2)
                    else:
                        next_state = (j1, 0)
                else:
                    if action[1] == 1:
                        amount = min(j1, jug2_cap - j2)
                        next_state = (j1 - amount, j2 + amount)
                    else:
                        amount = min(j2, jug1_cap - j1)
                        next_state = (j1 + amount, j2 - amount)
                # Add the next state to the queue if it has not been visited before
                if next_state not in visited:
                    next_seq = seq + [action]
                    queue.append((next_state[0], next_state[1], next_seq))
    # If the queue becomes empty without finding a solution, return None
    return None

result = water_jug_problem(5, 3, 1)
print(result)


                                                    
                                                    #experiment 03 Tic Tac Toe

# Set up the game board as a list
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

# Define a function to print the game board
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Define a function to handle a player's turn
def take_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a position from 1-9: ")
    position = int(position) - 1
    while board[position] != "-":
        position = int(input("Position already taken. Choose a different position: ")) - 1
    board[position] = player
    print_board()

# Define a function to check if the game is over
def check_game_over():
    # Check for a win
    if (board[0] == board[1] == board[2] != "-") or \
    (board[3] == board[4] == board[5] != "-") or \
    (board[6] == board[7] == board[8] != "-") or \
    (board[0] == board[3] == board[6] != "-") or \
    (board[1] == board[4] == board[7] != "-") or \
    (board[2] == board[5] == board[8] != "-") or \
    (board[0] == board[4] == board[8] != "-") or \
    (board[2] == board[4] == board[6] != "-"):
        return "win"
    # Check for a tie
    elif "-" not in board:
        return "tie"
    # Game is not over
    else:
        return "play"

# Define the main game loop
def play_game():
    print_board()
    current_player = "X"
    game_over = False
    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()


                                              # EXP 3 : CryptArthimetic Problem

from itertools import combinations, permutations
def replacements():
    for comb in combinations(range(10), 8):
        for perm in permutations(comb):
            if perm[0] * perm[1] != 0:
                yield dict(zip('BASELGMS', perm))
a, b, c = 'BASE', 'BALL', 'GAMES'
for replacement in replacements():
    f = lambda x: sum(replacement[e] * 10**i for i, e in enumerate(x[::-1]))
    if f(a) + f(b) == f(c):
        print('{} + {} = {}'.format(f(a), f(b), f(c)))


                                        #Exp 4 : Implementation and Analysis of BFS And DFS for Same Application

from collections import deque
# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
start_node = 'A'
visited_nodes = set()
print("DFS : ")
dfs(graph, start_node, visited_nodes)
print('\n')
print("BFS : ")
start_node = 'A'
bfs(graph, start_node)



                                                #EXP 5  ->BEST FIRST SEARCH

from queue import PriorityQueue

v = 14

graph = [[] for i in range(v)]

def best_first_search(source,destination,graph):
  pq = PriorityQueue()
  visited = [False] * 14
  visited[source] = True

  pq.put((0,source))

  while pq:
    node = pq.get()[1]
    print(node)
    if node==destination:
      break

    for v,c in graph[node]:
      if visited[v] ==False:
        visited[v] = True
        pq.put((c,v))

def addedge(x,y,cost):
  graph[x].append((y,cost))
  graph[y].append((x,cost))

addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

source = 0
destination = 9

best_first_search(source,destination,graph)



                                                #weak  ->  A*

from queue import PriorityQueue
class PuzzleState:
    def __init__(self, puzzle, parent=None, move="Initial", cost=0):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.cost = cost
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash(str(self.puzzle))

    def h(self):
        return sum([1 if self.puzzle[i][j] != self.goal_state[i][j] else 0 for i in range(3) for j in range(3)])

    def get_successors(self):
        successors = []
        empty_row, empty_col = self.find_empty_tile()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_puzzle = [row[:] for row in self.puzzle]
                new_puzzle[empty_row][empty_col], new_puzzle[new_row][new_col] = \
                    new_puzzle[new_row][new_col], new_puzzle[empty_row][empty_col]
                successors.append(PuzzleState(new_puzzle, self, "Move", self.cost + 1))

        return successors

    def find_empty_tile(self):
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    return i, j

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put(initial_state)
    explored = set()

    while not frontier.empty():
        current_state = frontier.get()
        if current_state.puzzle == current_state.goal_state:
            return current_state

        explored.add(current_state)
        for successor in current_state.get_successors():
            if successor not in explored:
                frontier.put(successor)

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found")
    else:
        path = []
        current_state = solution
        while current_state.parent:
            path.append((current_state.move, current_state.puzzle))
            current_state = current_state.parent
        path.append(("Initial", current_state.puzzle))

        path.reverse()
        for move, puzzle in path:
            print(move)
            print_puzzle(puzzle)

def print_puzzle(puzzle):
    for row in puzzle:
        print(row)
    print()

# Example usage:
initial_state = PuzzleState([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
solution = a_star_search(initial_state)
print_solution(solution)



#                   EXP 6 : To implement Bayesian Belief Networks to model the problem of Monty.

import random

def monty_hall_simulation(num_trials):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_trials):
        # print("")
        # print(f"{_} iteration ")
        doors = ['A', 'B', 'C']
        bike_location = random.choice(doors)
        # print("Bike location : ",bike_location)
        initial_choice = random.choice(doors)
        # print("player choice: ",initial_choice)
        doors.remove(initial_choice)

        if bike_location in doors:
            doors.remove(bike_location)
        monty_choice = random.choice(doors)

        # print("Monty's choice : ", monty_choice)
        doors = [d for d in ['A', 'B', 'C'] if d != monty_choice and d != initial_choice]
        final_choice = doors[0]

        stay_wins += (initial_choice == bike_location)
        switch_wins += (final_choice == bike_location)

    stay_win_prob = stay_wins / num_trials
    switch_win_prob = switch_wins / num_trials

    print(f"Probability of winning by staying: {stay_win_prob:.2f}")
    print(f"Probability of winning by switching: {switch_win_prob:.2f}")

# Number of trials
num_trials = 10

# Run simulation
monty_hall_simulation(num_trials)


                    #EXP 7 : Implementation of unification and resolution for real world problems.

def unify(statement1, statement2):
    # Split statements into words
    words1 = statement1.split()
    words2 = statement2.split()

    # Initialize an empty substitution dictionary
    substitution = {}

    # Iterate over the words in both statements
    for word1, word2 in zip(words1, words2):
        # If a word in statement 2 is a variable, assign its value based on statement 1
        if word2.isalpha() and word2[0].isupper():
            substitution[word2] = word1
        # If words don't match and neither is a variable, unification is not possible
        elif word1 != word2:
            return None

    # Return the substitution dictionary
    return substitution

# Given statements
statement1 = "Moksha and Vineela are sisters"
statement2 = "X and Y are sisters"

# Unify statement 2 with statement 1
result = unify(statement1, statement2)

# Print the result
if result:
    print("The unification is successful. Substitution =", result)
else:
    print("Unification failed.")



                                      #EXP 8 : Unsupervised Learning Methods

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


x = [1,2,2,1,8,9,8,9]
y = [1,2,1,2,8,9,9,8]

plt.scatter(x,y)
plt.show()


data = list(zip(x,y))
inertias = []

for i in range(1,8):
  kmeans = KMeans(n_clusters=i)
  kmeans.fit(data)
  inertias.append(kmeans.inertia_)

plt.plot(range(1,8),inertias,marker="o")
plt.show()


kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
plt.scatter(x,y,c=kmeans.labels_)
plt.show()


                                    #KNN  algorithm

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier



x = [1,2,2,1,8,9,8,9]
y = [1,2,1,2,8,9,9,8]
classes = [0,0,0,0,1,1,1,1]
plt.scatter(x,y,c=classes)
plt.show()

data = list(zip(x,y))
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(data,classes)

new_x = 8.5
new_y = 8.5

new_point = [(new_x,new_y)]
prediction = knn.predict(new_point)
print(prediction)

