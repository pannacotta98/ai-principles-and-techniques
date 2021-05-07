% TV PROBLEM

% CONTROL PARAMETERS
% Total order over the actions
% 	ordering(linear).
% Partial order over the actions
% 	ordering(partial).
%
% 	parallel(A,B).
% defines which actions can be executed in parallel, that is,
% there is no order among them

% Given a partial oreder plan, the directive
% 	derivedPlans(one).
% makes the planner to derive only one plan.
% In contrast,
% 	derivedPlans(all).
% makes the planner to derive all plans.

ordering(partial).
derivedPlans(all).

% ACTIONS:    action(Name,Prec,Del,Add)
action(study,[],[],[readyForExam]).
action(train,[badShape],[badShape],[goodShape,hungry]).
action(eat,[hungry],[hungry],[sated]).
action(watchTV,[],[],[watchedTV]).

parallel(watchTV, eat).
parallel(train, watchedTV).

% DOMAIN KNOWLEDGE
ags253g <- [].

% FLUENT
fluent(goodShape).
fluent(badShape).
fluent(readyForExam).
fluent(hungry).
fluent(sated).
fluent(watchedTV).

% INITIAL SITUATION
holds(badShape,init).