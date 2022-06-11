import os

from pyswip import Prolog



class Port:
    def __init__(self, inp_age, inp_ps, inp_p0, inp_p1, inp_p2, inp_p3, inp_p4,  inp_p5,  inp_p6, inp_p7,  inp_p8,  inp_p9,  inp_p10,  inp_p11,  inp_p12,  inp_p13,  inp_p14,  inp_p15,  inp_p16, inp_p17):
        self.inp_age = inp_age
        self.inp_ps = inp_ps
        self.inp_p0 = inp_p0
        self.inp_p1 = inp_p1
        self.inp_p2 = inp_p2
        self.inp_p3 = inp_p3
        self.inp_p4 = inp_p4
        self.inp_p5 = inp_p5
        self.inp_p6 = inp_p6
        self.inp_p7 = inp_p7
        self.inp_p8 = inp_p8
        self.inp_p9 = inp_p9
        self.inp_p10 = inp_p10
        self.inp_p11 = inp_p11
        self.inp_p12 = inp_p12
        self.inp_p13 = inp_p13
        self.inp_p14 = inp_p14
        self.inp_p15 = inp_p15 
        self.inp_p16 = inp_p16
        self.inp_p17 = inp_p17


    def create_query(self, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, ps, age):
        return "port:port_result(port(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s), %s, Result)." % ( p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, ps, age)

    
    def get_result(self):
        d = Prolog()
        file_path = os.path.abspath(__file__)
        edited_path = file_path[:-9].replace("\\", "/")
        d.consult(edited_path + 'port.pl')
        res = list(d.query(self.create_query(self.inp_age, self.inp_ps, self.inp_p0, self.inp_p1, self.inp_p2,self. inp_p3, self.inp_p4,  self.inp_p5,  self.inp_p6, self.inp_p7,  self.inp_p8,  self.inp_p9,  self.inp_p10,  self.inp_p11, self. inp_p12,  self.inp_p13,  self.inp_p14,  self.inp_p15, self.inp_p16, self.inp_p17)))
        x = res[0]['Result']
        return x


class Curb:
    def __init__(self, inp_age, inp_p0, inp_p1, inp_p2, inp_p3):
        self.inp_age = inp_age
        self.inp_p0 = inp_p0
        self.inp_p1 = inp_p1
        self.inp_p2 = inp_p2
        self.inp_p3 = inp_p3

    def create_query(self, p0, p1, p2, p3):
        return "curb:curb_result(curb(%s,%s,%s,%s), Result)." % ( p0, p1, p2, p3)

    def get_result(self):
        d = Prolog()
        file_path = os.path.abspath(__file__)
        edited_path = file_path[:-9].replace("\\", "/")
        d.consult(edited_path + 'curb.pl')
        res = list(d.query(self.create_query(self.inp_p0, self.inp_p1, self.inp_p2, self.inp_p3)))
        x = res[0]['Result']
        if int(self.inp_age) > 65:
            x += 1
        else:
            x += 0
        return x


class Smart:
    def __init__(self,  inp_p0, inp_p1, inp_p2, inp_p3, inp_p4,  inp_p5,  inp_p6, inp_p7,):
        self.inp_p0 = inp_p0
        self.inp_p1 = inp_p1
        self.inp_p2 = inp_p2
        self.inp_p3 = inp_p3
        self.inp_p4 = inp_p4
        self.inp_p5 = inp_p5
        self.inp_p6 = inp_p6
        self.inp_p7 = inp_p7


    def create_query(self, p0, p1, p2, p3, p4, p5, p6, p7):
        return "smart:smart_result(smart(%s,%s,%s,%s,%s,%s,%s,%s), Result)." % ( p0, p1, p2, p3, p4, p5, p6, p7)


    def get_result(self):
        d = Prolog()
        file_path = os.path.abspath(__file__)
        edited_path = file_path[:-9].replace("\\", "/")
        d.consult(edited_path + 'smart.pl')
        res = list(d.query(self.create_query(self.inp_p0, self.inp_p1, self.inp_p2,self. inp_p3, self.inp_p4,  self.inp_p5,  self.inp_p6, self.inp_p7)))
        x = res[0]['Result']
        return x