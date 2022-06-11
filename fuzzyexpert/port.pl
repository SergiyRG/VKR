:- module(port,[]).

port_p0(yes, X) :-
    X = 10.

port_p0(no, X) :-
    X = 0.



port_p1(yes, X) :-
    X = 30.

port_p1(no, X) :-
    X = 0.



port_p2(yes, X) :-
    X = 20.

port_p2(no, X) :-
    X = 0.



port_p3(yes, X) :-
    X = 10.

port_p3(no, X) :-


    X = 0.

port_p4(yes, X) :-
    X = 10.

port_p4(no, X) :-


    X = 0.

port_p5(yes, X) :-
    X = 10.

port_p5(no, X) :-
    X = 0.



port_p6(yes, X) :-
    X = 20.

port_p6(no, X) :-
    X = 0.



port_p7(yes, X) :-
    X = 20.

port_p7(no, X) :-
    X = 0.



port_p8(yes, X) :-
    X = 20.

port_p8(no, X) :-
    X = 0.



port_p9(yes, X) :-
    X = 15.

port_p9(no, X) :-
    X = 0.



port_p10(yes, X) :-
    X = 10.

port_p10(no, X) :-
    X = 0.



port_p11(yes, X) :-
    X = 30.

port_p11(no, X) :-
    X = 0.



port_p12(yes, X) :-
    X = 20.

port_p12(no, X) :-
    X = 0.



port_p13(yes, X) :-
    X = 20.

port_p13(no, X) :-
    X = 0.



port_p14(yes, X) :-
    X = 10.

port_p14(no, X) :-
    X = 0.



port_p15(yes, X) :-
    X = 10.

port_p15(no, X) :-
    X = 0.



port_p16(yes, X) :-
    X = 10.

port_p16(no, X) :-
    X = 0.


port_p17(yes, X) :-
    X = 10.

port_p17(no, X) :-
    X = 0.

port_sex(men, X) :-
    X = 0.

port_sex(women, X) :-
    X = 10.
 
port_result(port(P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,PS), Age, Result) :-
    port_p0(P0,X0),
    port_p1(P1,X1),
    port_p2(P2,X2),
    port_p3(P3,X3),
    port_p4(P4,X4),
    port_p5(P5,X5),
    port_p6(P6,X6),
    port_p7(P7,X7),
    port_p8(P8,X8),
    port_p9(P9,X9),
    port_p10(P10,X10),
    port_p11(P11,X11),
    port_p12(P12,X12),
    port_p13(P13,X13),
    port_p14(P14,X14),
    port_p15(P15,X15),
    port_p16(P16,X16),
    port_p17(P17,X17),
    port_sex(PS, SX),

    Result is Age - SX + (X0 + X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 + X9 + X11 + X12 + X13 + X14 + X15 + X16 + X17).
    
    

