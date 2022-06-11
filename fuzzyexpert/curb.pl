:-module(curb, []).

curb_p0(yes, X) :-
    X = 1.

curb_p0(no, X) :-
    X = 0.

curb_p1(yes, X) :-
    X = 1.

curb_p1(no, X) :-
    X = 0.


curb_p2(yes, X) :-
    X = 1.

curb_p2(no, X) :-
    X = 0.


curb_p3(yes, X) :-
    X = 1.

curb_p3(no, X) :-
    X = 0.



curb_result(curb(P0,P1,P2,P3),Result) :-
    curb_p0(P0, X0),
    curb_p1(P1, X1),
    curb_p2(P2, X2),
    curb_p3(P3, X3),

    Result is X0 + X1 + X2 + X3.
