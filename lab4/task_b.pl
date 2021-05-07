:- use_module(library(clpfd)).

square(X) :- X in 2..4 \/ 6.
triangle(X) :- X in 1 \/ 5.
red(X) :- X in 1 \/ 4.
green(X) :- X in 2 \/ 5.
blue(X) :- X in 3 \/ 6.
table(X) :- X in 0.

% X is the block to move, A is the block under X, and B is the block to put X on
act(move(X,A,B),
  [on(X,A), pickable(X), pickable(B)], % preconditions
  [on(X,A), pickable(B)], % delete
  [on(X,B), pickable(A)] % add
  ):-
  square(B),
  A #\= B.


initial_state([    
    on(3, 4),
    on(5, 6),
    on(1, 0),
    on(2, 0),
    on(4, 0),
    on(6, 0),

    pickable(1),
    pickable(2),
    pickable(3),
    pickable(5)
]).

goal_state([
  on(X,Y),
  on(Y,Z)
  ]):-
  green(Y),
  blue(Z).