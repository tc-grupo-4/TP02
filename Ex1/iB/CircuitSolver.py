from sympy import Symbol
from sympy import Function, simplify
from sympy import *
from sympy import init_printing
from sympy.core.numbers import pi, I, oo
from sympy import re, im
from sympy.solvers.inequalities import solve_rational_inequalities
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy.solvers import solve
import matplotlib.pyplot as plt
import math
import numpy as np



class circuitSolver:
    def __init__(self):
        self.equations = None
        self.unknowns = None
        self.H=None
        self.zinp = None
        self.zout = None
        self.solution = None
        self.Vi =Symbol('Vi',real = True, positive = True)
        self.Vo = Symbol('Vo',real = True, positive = True)
        return

    def setEquations(self,equationsList):
        self.equations = equationsList
        return

    def setUnknowns(self,unknownsList): ##Tienen que estar si o si Vi y Vo como unknowns
        self.unknowns = unknownsList
        return
    
    def solveCircuit(self):
        self.solution = solve(self.equations,self.unknowns)
        return

    def getH(self):
        self.h = self.solution[self.Vo]/self.solution[self.Vi]
        self.h = simplify(self.h)
        return self.h

    def getUnknowns(self):
        return self.solution

    def calcZinp(self,inpCurr):
        self.zinp = simplify(self.solution[self.Vi]/inpCurr)
        return self.zinp
        
    def calcZout(self,outCurr):

        self.zout = simplify(self.solution[self.Vo]/outCurr)
        return self.zout
    
    def getZinp(self):
        return self.zinp

    def getZout(self):
        return self.zout

    def reset(self):
        self.equations = None
        self.unknowns = None
        self.H=None
        self.zinp = None
        self.zout = None
        self.solution = None
        return


def main():
    
    
    test = circuitSolver()
    equations = []
    Aw = a0/(1+s/w)
    
    equations.append(((Vi-Vp)/r3)-Vp/r4)
    equations.append((Vo-Vm)/r2-(Vm/r1))
    equations.append(Vo - Aw*(Vp-Vm))

    unknowns = [Vi,Vo,Vp]
    test.setEquations(equations)
    test.setUnknowns(unknowns)
    test.solveCircuit()
    H = test.getH()
    inpCurr = (test.getUnknowns()[Vi]-test.getUnknowns()[Vp]) / r3
    test.calcZinp(inpCurr)
    unknowns = [Vi,Vo,Vm]
    test.setUnknowns(unknowns)
    test.solveCircuit()
    outCurr = (test.getUnknowns()[Vo]-test.getUnknowns()[Vm]) / r2
    test.calcZout(outCurr)
    print(substitute(test.getZinp(),3))
    

def substitute(express, case):
    express = express.subs(w,7.5* 2 * 3.142)        ##check
    express = express.subs(a0,100000)        ##check
    if case == 1:
        express = express.subs(r1,10000)
        express = express.subs(r3,10000)
        express = express.subs(r2,100000)
        express = express.subs(r4,40000)
    elif case == 2:
        express = express.subs(r1,10000)
        express = express.subs(r3,10000)
        express = express.subs(r2,10000)
        express = express.subs(r4,40000)
    elif case == 3:
        express = express.subs(r1,100000)
        express = express.subs(r3,100000)
        express = express.subs(r2,10000)
        express = express.subs(r4,400000)
    express = simplify(express)
    return express


init_printing()
a0 = Symbol('a0',real = True, positive = True)
r1 = Symbol('R1',real = True, positive = True)
r2 = Symbol('R2',real = True, positive = True)
r3 = Symbol('R3',real = True, positive = True)
r4 = Symbol('R4',real = True, positive = True)
w = Symbol('W',real = True, positive = True)
f = Symbol('f',real = True, positive = True)
Vi = Symbol('Vi',real = True, positive = True)
Vo = Symbol('Vo',real = True, positive = True)
Vp = Symbol('Vp',real = True, positive = True)
Vm = Symbol('Vm',real = True, positive = True)
s = Symbol('s')
main()
