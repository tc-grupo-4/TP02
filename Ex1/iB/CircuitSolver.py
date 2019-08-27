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
        self.mod = None
        self.phase = None
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
        self.H = self.solution[self.Vo]/self.solution[self.Vi]
        self.H = simplify(self.H)
        self.mod = simplify(sqrt(re(self.H)**2+im(self.H)**2))
        self.phase = simplify(tan(im(self.H)/re(self.H))*180/3.14195)
        return self.H
    
    def getMod(self):
        self.H = self.solution[self.Vo]/self.solution[self.Vi]
        self.H = simplify(self.H)
        self.mod = simplify(sqrt(re(self.H)**2+im(self.H)**2))
        self.phase = simplify(tan(im(self.H)/re(self.H))*180/3.14195)
        return self.mod

    def getPhase(self):
        self.H = self.solution[self.Vo]/self.solution[self.Vi]
        self.H = simplify(self.H)
        self.mod = simplify(sqrt(re(self.H)**2+im(self.H)**2))
        self.phase = simplify(tan(im(self.H)/re(self.H))*180/3.14195)
        return self.phase

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
