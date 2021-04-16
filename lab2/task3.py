
# def min_conflicts(csp, max_steps=100000):
#     """Solve a CSP by stochastic hillclimbing on the number of conflicts."""
#     # Generate a complete assignment for all variables (probably with conflicts)
#     csp.current = current = {}
#     for var in csp.variables:
#         val = min_conflicts_value(csp, var, current)
#         csp.assign(var, val, current)
#     # Now repeatedly choose a random conflicted variable and change it
#     for i in range(max_steps):
#         conflicted = csp.conflicted_vars(current)
#         if not conflicted:
#             return current
#         var = random.choice(conflicted)
#         val = min_conflicts_value(csp, var, current)
#         csp.assign(var, val, current)
#     return None


# def min_conflicts_value(csp, var, current):
#     """Return the value that will give var the least number of conflicts.
#     If there is a tie, choose at random."""
#     return argmin_random_tie(csp.domains[var],
#                              key=lambda val: csp.nconflicts(var, val, current))

import random as rand

class Booking:
    def __init__(self, block, courses):
        self.room = block[0]
        self.time = block[1]
        self.conflicts = -1
        self.course = rand.choice(courses)
        courses.remove(self.course)

    def will_miss_course(self, other):
        if self.time == other.time:
            if self.course[2] == other.course[2] and (not self.course[2] == '5' or not other.course[2] == '5'):
                return True
        return False

    def is_double_booked(self, other):
        return self.room == other.room and self.time == other.time

    def find_n_conflicts(self, all_other):
        counter = -1
        for booking in all_other:
            if self.is_double_booked(booking):
                counter += 1
            if self.will_miss_course(booking):
                counter += 1
        self.conflicts = counter
        return self.conflicts

    def __str__(self):
        print(self.room + ", " + str(self.time) + ", " + self.course)

def print_timetable(bookings):
    bookings.sort(key = lambda booking: booking.time)
    print("\n     TP51    SP34    K3\n-----------------------------")
    i = 0
    while i < len(bookings):
        sub_array = bookings[i:i+3]
        sub_array.sort(key = lambda booking: booking.room)

        if len(sub_array) == 3:
            print(str('{:>2}'.format(sub_array[0].time)) + "   " + sub_array[2].course + "   " + sub_array[1].course + "   " + sub_array[0].course)
        if len(sub_array) == 2:
            print(str('{:>2}'.format(sub_array[0].time)) + "   " + sub_array[1].course + "   " + sub_array[0].course)
        if len(sub_array) == 1:
            print(str('{:>2}'.format(sub_array[0].time)) + "   " + sub_array[0].course)
        i += 3


rooms = ['TP51', 'SP34', 'K3']
times = [9, 10, 11, 12, 13, 14, 15, 16]

courses = [
    'MT101','MT102','MT103','MT104','MT105','MT106','MT107',
    'MT201','MT202','MT203','MT204','MT205','MT206',
    'MT301','MT302','MT303','MT304',
    'MT401','MT402','MT403',
    'MT501','MT502'
]

blocks = []
for room in rooms:
    for time in times:
        blocks.append((room, time))


MAX_STEPS = 10000
n_conflicts = 0
bookings = []
for i in range(0, len(courses)):
    bookings.append(Booking(blocks[i], courses))

courses = [
'MT101','MT102','MT103','MT104','MT105','MT106','MT107',
'MT201','MT202','MT203','MT204','MT205','MT206',
'MT301','MT302','MT303','MT304',
'MT401','MT402','MT403',
'MT501','MT502'
]

for booking in bookings:
    booking.find_n_conflicts(bookings)

rand_booking = None
for i in range(0, MAX_STEPS):
    n_conflicts = 0
    for booking in bookings:
        booking.find_n_conflicts(bookings)
        n_conflicts += booking.conflicts
    # print(n_conflicts)
    if n_conflicts == 0:
        print_timetable(bookings)
        quit()
    
    rand_booking = rand.choice([book for book in bookings if book.conflicts > 0 and book != rand_booking])

    lowest_conflicts = rand_booking.conflicts
    best_course = rand_booking.course
    for course in courses:
        tmp_booking = rand_booking
        tmp_booking.course = course
        tmp_conflicts = tmp_booking.find_n_conflicts(bookings)

        if tmp_conflicts < lowest_conflicts:
            best_course = course
            lowest_conflicts = tmp_conflicts
    
    bookings[bookings.index(rand_booking)].course, courses[courses.index(best_course)] = \
        courses[courses.index(best_course)], bookings[bookings.index(rand_booking)].course

print('Failed to create non-conflicting timetable in {} number of steps'.format(MAX_STEPS))