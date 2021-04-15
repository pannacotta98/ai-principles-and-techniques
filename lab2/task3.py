
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
    def __init__(self, room, time, courses):
        self.room = room
        self.time = time
        self.course = rand.choice(courses)
        self.conflicts = -1

        # courses.remove(self.course)

    def will_miss_course(self, other):
        if not self.course == 'MT501' and not self.course == 'MT502' and not other.course == 'MT501' and not other.course == 'MT502':
            if self.time == other.time and self.course[2] == other.course[2]:
                return True
        return False

    def is_double_booked(self, other):
        return self.room == other.room and self.time == other.time

    def find_n_conflicts(self, all_other):
        counter = -1
        for booking in all_other:
            if self.is_double_booked(booking) or self.will_miss_course(booking):
                counter += 1
        self.conflicts = counter

    def __str__(self):
        print(self.room + ", " + str(self.time) + ", " + self.course)


variables = ['TP51', 'SP34', 'K3']
times = [9, 10, 11, 12, 13, 14, 15, 16]
courses = ['MT101','MT102','MT103','MT104','MT105','MT106','MT107','MT201','MT202','MT203','MT204','MT205','MT206','MT301','MT302','MT303','MT304'\
        ,'MT401','MT402','MT403','MT404','MT501','MT502']

MAX_STEPS = 100
n_conflicts = 0
bookings = []
for i in range(0, 23):
    bookings.append(Booking(rand.choice(variables), rand.choice(times), courses))

for booking in bookings:
    booking.find_n_conflicts(bookings)

for i in range(0, MAX_STEPS):
    for booking in bookings:
        n_conflicts += booking.conflicts
    if n_conflicts == 0:
        print(bookings)
        quit()
    rand_booking = rand.choice(bookings)

    # Find value for rand_booking which minimizes n_conflicts