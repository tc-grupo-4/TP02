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

def main():
    h = getH()
    h1 = substitute(h,3)
    print(latex(h1))
def getH(): 
    equations = []
    Aw = a0/(1+s/w)
    equations.append(((Vi-Vp)/r3)-Vp/r4)
    equations.append((Vo-Vm)/r2-(Vm/r1))
    equations.append(Vo - Aw*(Vp-Vm))
    unknowns = [Vi,Vo,Vp]
    sol = solve(equations,unknowns)
    h=sol[Vo]/sol[Vi]
    h = simplify(h)
    return h


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