remove_dup([],[]).

remove_dup(List, Set) :-
     remove_dup_helper(List, [], Set).

remove_dup_helper([], Acc, Acc).

remove_dup_helper([H|T], Acc, Set) :-
     member(H, Acc),
     remove_dup_helper(T, Acc, Set).

remove_dup_helper([H|T], Acc, Set) :-
     NewAcc = [H|Acc],
     remove_dup_helper(T, NewAcc, Set).



append2([], E, [E]).
append2([H | T], H, [H | T]) :-
    !.
append2([H | T], E, [E, H | T]) :-
    !.

merge2([], [], []).
merge2([], X, Xr) :-
    remove_dup(X, Xr).

merge2(X, [], Xr) :-
    remove_dup(X, Xr).

merge2([H1 | T1], [H2 | T2], X) :-
    H2 >= H1,
    merge2(T1, [H2 | T2], Tr),
    append2(Tr, H1, X).

merge2([H1 | T1], [H2 | T2], X) :-
    H1 > H2,
    merge2([H1 | T1], T2, Tr),
    append2(Tr, H2, X).

merge_hetero([], []).

merge_hetero([H | T], Tr) :-
    number(H),
    merge_hetero(T, Tr).

merge_hetero([H | T], X) :-
    is_list([H | T]),
    merge_hetero(T, Y),
    merge2(H, Y, X).

