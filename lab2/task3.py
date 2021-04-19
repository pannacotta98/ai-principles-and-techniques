from collections import namedtuple
import random as rand

MAX_STEPS_TASK_4 = 300
solutions = []

def count_num_pref_times(solution):
    counter = 0
    if solution[RoomSlot("TP51", 9)] == '     ':
        counter += 1
    if solution[RoomSlot("SP34", 9)] == '     ':
        counter += 1
    if solution[RoomSlot("K3", 9)] == '     ':
        counter += 1
    if solution[RoomSlot("TP51", 12)] == '     ':
        counter += 1
    if solution[RoomSlot("SP34", 12)] == '     ':
        counter += 1
    if solution[RoomSlot("K3", 12)] == '     ':
        counter += 1
    if solution[RoomSlot("TP51", 16)] == '     ':
        counter += 1
    if solution[RoomSlot("SP34", 16)] == '     ':
        counter += 1
    if solution[RoomSlot("K3", 16)] == '     ':
        counter += 1
        
    return counter

def count_pref_mt500_times(solution):
    counter = 0
    if solution[RoomSlot("TP51", 13)] == 'MT501' or solution[RoomSlot("TP51", 13)] == 'MT502':
        counter += 1
    if solution[RoomSlot("SP34", 13)] == 'MT501' or solution[RoomSlot("SP34", 13)] == 'MT502':
        counter += 1
    if solution[RoomSlot("K3", 13)] == 'MT501' or solution[RoomSlot("K3", 13)] == 'MT502':
        counter += 1
    if solution[RoomSlot("TP51", 14)] == 'MT501' or solution[RoomSlot("TP51", 14)] == 'MT502':
        counter += 1
    if solution[RoomSlot("SP34", 14)] == 'MT501' or solution[RoomSlot("SP34", 14)] == 'MT502':
        counter += 1
    if solution[RoomSlot("K3", 14)] == 'MT501' or solution[RoomSlot("K3", 14)] == 'MT502':
        counter += 1
    return counter

def print_timetable(state):
        '''Print timetable. Currently dependent on the global variable `time_slots`'''
        print()
        print('      TP51     SP34     K3')
        print('      ----     ----     ----')
        for time_slot in time_slots:
            print('{:<2}    {}    {}    {}'.format(
                time_slot, 
                state[('TP51', time_slot)],
                state[('SP34', time_slot)],
                state[('K3', time_slot)]))
        print()

for i in range(0, MAX_STEPS_TASK_4):
    MAX_STEPS = 100

    rooms = ['TP51', 'SP34', 'K3']
    time_slots = [9, 10, 11, 12, 13, 14, 15, 16]
    courses = [
        'MT101','MT102','MT103','MT104','MT105','MT106','MT107',
        'MT201','MT202','MT203','MT204','MT205','MT206',
        'MT301','MT302','MT303','MT304',
        'MT401','MT402','MT403',
        'MT501','MT502',
        '     ','     ' # Empty slots
    ]

    RoomSlot = namedtuple('RoomSlot', ['room', 'time'])


    def bookings_conflict(slot1, course1, slot2, course2):
        '''Checks if two bookings are in conflict'''
        if course1[2] == 5 and course2[2] == 5:
            return False
        return slot1.time == slot2.time and course1[2] == course2[2]


    def is_solution(state):
        for slot1 in state:
            for slot2 in state:
                if bookings_conflict(slot1, state[slot1], slot2, state[slot2]) and slot1 != slot2:
                    return False
        return True


    def conflicts(var, v, swap_with_key, state):
        # Swap to test the conflicts if keys are swapped
        dict_swap(var, swap_with_key, current_state)

        counter = 0
        for slot in state:
            if bookings_conflict(var, v, slot, state[slot]) and slot != var:
                counter += 1

        # Swap back
        dict_swap(var, swap_with_key, current_state)

        return counter


    def dict_swap(key1, key2, dict):
        dict[key1], dict[key2] = dict[key2], dict[key1]


    # Find all time blocks for all rooms
    blocks = []
    for time in time_slots:
        for room in rooms:
            blocks.append(RoomSlot(room, time))

    # Generate a random initial state
    # Copy so the courses can be removed without affecting `courses`
    courses_to_distribute = [c for c in courses]
    rand.shuffle(courses_to_distribute)
    current_state = {}
    for block in blocks:
        current_state[block] = courses_to_distribute.pop()

    # print_timetable(current_state)

    for i in range(MAX_STEPS):
        if is_solution(current_state):
            solutions.append(current_state)
            break

        # TODO Make sure that var is actually in conflict
        # var = rand.choice(list(current_state.keys()))
        var = rand.choice(
            [v for v in list(current_state.keys())
                if conflicts(v, current_state[v], v, current_state) > 0])

        # Find value that minimizes conflicts
        min_conflicts_val = None
        min_conflicts_swap_key = None
        min_conflicts = 1e9
        for key in current_state:
            v = current_state[key]
            n_conf = conflicts(var, v, key, current_state)
            if n_conf < min_conflicts:
                min_conflicts = n_conf
                min_conflicts_val = v
                min_conflicts_swap_key = key

        # Swap
        dict_swap(var, min_conflicts_swap_key, current_state)

print("Solutions found, finding the most preferable schedule:")
max_pref_conflicts = -1
best_solution = None
for solution in solutions:
    tmp_pref_conflicts = 0
    tmp_pref_conflicts += count_num_pref_times(solution)
    tmp_pref_conflicts += count_pref_mt500_times(solution)

    if tmp_pref_conflicts > max_pref_conflicts:
        max_pref_conflicts = tmp_pref_conflicts
        best_solution = solution
print_timetable(best_solution)