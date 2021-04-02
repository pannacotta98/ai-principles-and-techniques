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


class Node:
    def __init__(self, state, g, h):
        self.g = g
        self.h = h
        self.state = state

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + self.g)

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


rands = random.sample(range(0, 9, 1), 9)
init_state = [[rands[0], rands[1], rands[2]], [
    rands[3], rands[4], rands[5]], [rands[6], rands[7], rands[8]]]


start_node = Node(init_state, 0, num_misplaced_tiles(init_state))
goal_node = Node(GOAL_STATE, 0, 0)

print("Starting node:")
print(start_node)

open_list = [start_node]  # All nodes that must still be expanded
closed_list = []  # Has been visited

print("Running...")
start_time = time.clock_gettime(time.CLOCK_MONOTONIC)
while len(open_list) > 0:
    q = heapq.heappop(open_list)

    possible_moves = q.find_possible_moves()
    for move in possible_moves:
        if move.is_goal_state():
            print('REACHED GOAL, state:')
            print(move)
            print("Elapsed time: " +
                  str(round(time.clock_gettime(time.CLOCK_MONOTONIC) - start_time)) + " seconds.")
            quit()

        is_in_closed_list = False
        for state in closed_list:
            if identical_state(move.state, state):
                is_in_closed_list = True
                break

        is_in_open_list = False
        for node in open_list:
            if identical_state(move.state, node.state):
                is_in_open_list = True
                break

        if not is_in_closed_list and not is_in_open_list:
            heapq.heappush(open_list, move)

    closed_list.append(q.state)
