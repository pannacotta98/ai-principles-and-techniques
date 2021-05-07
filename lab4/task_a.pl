act(go(X,Y),
  [connect(X,Y), shakey(S), in(S,X), on(S,floor)], % preconditions
  [in(S,X)], % delete
  [in(S,Y)] % add
  ).
             
act(push(B,X,Y),
  [shakey(S), on(S, floor), box(B), in(S,X), in(B,X), connect(X,Y)],
  [in(S,X), in(B,X)],
  [in(S,Y), in(B,Y)]
  ).
  
act(climb_up(B),
  [shakey(S), box(B), on(S, floor), in(S,X), in(B,X)],
  [on(S, floor)],
  [on(S, B)]
  ).

act(climb_down(B),
  [shakey(S), box(B), on(S,B), in(S,X), in(B,X)],
  [on(S,floor)],
  [on(S,B)]
  ).
  
act(turn_on_light(Switch),
  [shakey(S), light(Switch, false), on(S,B), in(S,X), in(B,X)],
  [light(Switch, false)],
  [light(Switch, true)]
  ).
  
act(turn_off_light(Switch),
  [shakey(S), light(Switch, true), on(S,B), in(S,X), in(B,X)],
  [light(Switch, true)],
  [light(Switch, false)]
  ).


goal_state([
  in(s, room1),
  light(switch1, false),
  in(box2, room2)
  ]).
             
initial_state([
   shakey(s),
   in(s, room3),
   on(s, floor),

   box(box1),
   box(box2),
   box(box3),
   box(box4),

   room(room1),
   room(room2),
   room(room3),
   room(room4),
   room(corridor),

   in(box1, room1),
   in(box2, room1),
   in(box3, room1),
   in(box4, room1),

   light(switch1, true),
   light(switch2, false),
   light(switch3, false),
   light(switch4, true),

   connect(switch1, room1),
   connect(room1, switch1),
   connect(switch2, room2),
   connect(room2, switch2),
   connect(switch3, room3),
   connect(room3, switch3),
   connect(switch4, room4),
   connect(room4, switch4),

   connect(room1, corridor),
   connect(corridor, room1),
   connect(room2, corridor),
   connect(corridor, room2),
   connect(room3, corridor),
   connect(corridor, room3),
   connect(room4, corrdior),
   connect(corridor, room4)
]).
              
