:- module(smart, []).

s_p0(yes, X) :-
    X = 2.

s_p0(no, X) :-
    X = 0.

s_p1(yes, X) :-
    X = 1.

s_p1(no, X) :-
    X = 0.

s_p2(yes, X) :-
    X = 1.

s_p2(no, X) :-
    X = 0.


s_p3(yes, X) :-
    X = 1.

s_p3(no, X) :-
    X = 0.

s_p4(yes, X) :-
    X = 1.

s_p4(no, X) :-
    X = 0.


s_p5(yes, X) :-
    X = 1.

s_p5(no, X) :-
    X = 0.


s_p6(yes, X) :-
    X = 2.

s_p6(no, X) :-
    X = 0.


s_p7(yes, X) :-
    X = 2.

s_p7(no, X) :-
    X = 0.


smart_result(smart(P0,P1,P2,P3,P4,P5,P6,P7), Result) :-
    s_p0(P0,X0),
    s_p1(P1,X1),
    s_p2(P2,X2),
    s_p3(P3,X3),
    s_p4(P4,X4),
    s_p5(P5,X5),
    s_p6(P6,X6),
    s_p7(P7,X7),

    Result is X0 + X1 + X2 + X3 + X4 + X5 + X6 + X7.

