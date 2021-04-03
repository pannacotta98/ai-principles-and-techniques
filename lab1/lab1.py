import heapq
import random
import time

# 0 is empty tile
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
POSSIBLE_MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def identical_state(state1, state2):
    for i in range(0, 3):
        for j in range(0, 3):
            if not state1[i][j] == state2[i][j]:
                return False
    return True


def index_in_nested_list(arr, val):
    pos = (None, None)
    for i in range(0, len(arr)):
        try:
            idx = arr[i].index(val)
            pos = (i, idx)
            break
        except:
            pass
    return pos


def copy_and_swap(state, pos, move):
    x = pos[0] + move[0]
    y = pos[1] + move[1]
    if(0 <= x < 3 and 0 <= y < 3):
        copy = [row[:] for row in state]

        copy[pos[0]+move[0]][pos[1]+move[1]], copy[pos[0]][pos[1]] \
            = copy[pos[0]][pos[1]], copy[pos[0]+move[0]][pos[1]+move[1]]

        return copy
    return None


def num_misplaced_tiles(state):
    counter = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if not state[i][j] == GOAL_STATE[i][j] and not state[i][j] == 0:
                counter += 1
    return counter

def isSolvable(state):
    inv_count = 0
    flattened = [item for sublist in state for item in sublist]

    for i in range(0, len(flattened) - 1):
        for j in range(i + 1, len(flattened)):
            if flattened[i] > 0 and flattened[j] > 0 and flattened[j] > flattened[i]:
                inv_count += 1
    return inv_count % 2 == 0


class Node:
    def __init__(self, state, g, h):
        self.g = g
        self.h = h
        self.state = state

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def __str__(self):
        return "g: " + str(self.g) + "\n" + \
            "h: " + str(self.h) + "\n" \
            + str(self.state[0]) + "\n" + \
            str(self.state[1]) + "\n" + str(self.state[2])

    def find_possible_moves(self):
        open_pos = index_in_nested_list(self.state, 0)
        possible_moves = []
        for move in POSSIBLE_MOVES:
            possible_moves.append(copy_and_swap(self.state, open_pos, move))
        possible_moves = [move for move in possible_moves if not move == None]

        nodes = [Node(state, self.g + 1, num_misplaced_tiles(state))
                 for state in possible_moves]

        return nodes

    def is_goal_state(self):
        return identical_state(self.state, GOAL_STATE)

# Generate solvable puzzle
print("\n\nGenerating solvable puzzle...")
init_state = [[]]
while True:
    rands = random.sample(range(0, 9, 1), 9)
    init_state = [[rands[0], rands[1], rands[2]], [
    rands[3], rands[4], rands[5]], [rands[6], rands[7], rands[8]]]

    if isSolvable(init_state):
        break

start_node = Node(init_state, 0, num_misplaced_tiles(init_state))
goal_node = Node(GOAL_STATE, 0, 0)

print("Starting node:")
print(start_node)

open_list = [start_node]  # All nodes that must still be expanded
closed_list = []  # Has been visited

print("Solving...")
start_time = time.perf_counter()
while len(open_list) > 0:
    heapq.heapify(open_list)
    q = heapq.heappop(open_list)

    possible_moves = q.find_possible_moves()
    for move in possible_moves:
        if move.is_goal_state():
            print('REACHED GOAL, state:')
            print(move)
            print("Elapsed time: " +
                  str(round(time.perf_counter() - start_time)) + " seconds.")
            quit()

        state_has_been_seen = False
        for state in closed_list:
            if identical_state(move.state, state):
                state_has_been_seen = True
                break

        if not state_has_been_seen:
            for node in open_list:
                if identical_state(move.state, node.state):
                    state_has_been_seen = True
                    break

        if not state_has_been_seen:
            heapq.heappush(open_list, move)
    closed_list.append(q.state)
