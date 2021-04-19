"""  TASK 1/LAB2  TNM096 
     Run the various CSP solvers on selected Sudoku puzzles   """

from time import time
from datetime import timedelta
from aima.csp import Sudoku, AC3, backtracking_search, mrv, forward_checking, min_conflicts
from aima.search import depth_first_graph_search    
  
def secondsToStr(t):
    return str(timedelta(seconds=t))
def now():
    return secondsToStr(time())

print("\nSetting up the puzzle at\n     "+now()[12:20])
print("\nStart:")


# 1. Set up the puzzle; select ONLY one of the following problem specifications

# ------ solved
#puzzle = Sudoku('483921657967345821251876493548132976729564138136798245372689514814253769695417382')  #solved

# ------ easy
puzzle = Sudoku('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    # depth-first-graph-search: failed
    # backtracking search: 34 seconds
    # AC3: 0.023 seconds - failed
    # min conflicts: failed - 71 seconds
    # depth first graph search < min conflicts < backtracking search < AC3

# ------ harder
# puzzle = Sudoku('4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
    # depth-first-graph-search: too long
    # backtracking search: too long
    # AC3: failed very fast
    # min conflicts: failed
    # depth first graph search < min conflicts < backtracking search < AC3

# ------ hardest
# puzzle = Sudoku('1....7.9..3..2...8..96..5....53..9...1..8...26....4...3......1..4......7..7...3..')

puzzle.display(puzzle.infer_assignment())
start = time()

# Task (a):
    # Depth first search has an enourmous amount of leaves to search for solutions
    # It's an unintelligent brute force algorithm
    # This makes it unfeasible to use, the search tree is too large

    # Backtracking search is an expansion of depth first search which makes it slightly smarter
    # Since it immedidiately discards and subtrees with inconsistencies it significantly reduces the search tree
    # This gives it the second best performance on the easiest puzzle.

    # AC3 can only solve easy sudoku puzzles.
    # It solves the easiest one very fast and fails the harder one very fast

    # Min-conflicts

# Task (b):
    # BT: 34 sec
    # BT + FC: 0.01 sec (Forward checking)
    # BT + LCV: 1 min 4 sec (Least constraining value)
    # BT + MRV: Too long (Minimum remaining values)
    # BT + FC + MRV: 0.008 sec
    # BT + FC + LCV: 0.02 sec
    # BT + FC + LCV + MRV: 0.008 sec

    # The best heuristic setting for backtracking is forward checking + minimum remaining values (BT + FC + MRV)
    # Forward checking is the most important heuristic for reducing computation time
    # Combining forward checking with minimum remaining values reduced computational time further

# 2. Solve the puzzle; select ONLY one of the following algorithms

# depth_first_graph_search(puzzle)
# backtracking_search(puzzle)
AC3(puzzle)
# min_conflicts(puzzle)


# 3. Print the results
print("")
if puzzle.goal_test(puzzle.infer_assignment()):
    print("Solution:")
    puzzle.display(puzzle.infer_assignment())
else:
    print("Failed - domains: ")
    #print str(puzzle.curr_domains)

    
# 4. Print elapsed time
end = time()
elapsed = end-start
print("\nElapsed time ",  secondsToStr(elapsed)[0:15])

