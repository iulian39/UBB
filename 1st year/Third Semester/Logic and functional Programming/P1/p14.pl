% Write a predicate to test equality of two sets without using the set difference.
% we make the sum of each set and we compare it. if the sum of the sets
% is equal, then, the sets are equal

% main_compare(L1-list, L2- list)
% main_compare flow model (i,i)

%copy_list([],[]).
%copy_list([H|T1],[H|T2]) :- copy_list(T1,T2).

compare_list([],[]).
compare_list([],_).

compare_list([H|T], List2):-
    member(H, List2),
    compare_list(T, List2).


main_compare(List1, List2) :-
	length(List1, N),
    length(List2, M),
	(N = M ->
        compare_list(List1, List2)
	).

test:-
	main_compare([1,2,3],[2,1,3]), %true
        \+ main_compare([1,2,3], [1,2,3,4]),
        main_compare([],[]),
	getNth([1,2,3],1, 1),
        \+ getNth([1,2,3],10, _),
        \+ getNth([1,2,3], -1, _).

% Write a predicate to select the n-th element of a given list.
% getNth(L1-list, N - nr, X - variable)
% getNth flow model (i,i, o)

getNth([H | _], 1, H).

getNth([_ | T], N, X) :-
    N > 1,
    N1 is N - 1,
    getNth(T, N1, X).

