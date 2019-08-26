from sympy import Symbol
from sympy import Function, simplify
from sympy import *
from sympy import init_printing
from sympy.core.numbers import pi, I, oo
from sympy import re, im
from sympy.solvers.inequalities import solve_rational_inequalities
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy.solvers import solve
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def main():
    K = (r2*a0*w*(r3+r1)-w*(a0-1)*(r2*r3+r1*r2+r1*r3)) / (r2*a0*w-(r2+r3)*w*(a0-1))
    C = (w*(a0-1)*(r2*r3+r1*r2+r1*r3)-r2*a0*w*(r3+r1))/(r2*r3+r1*r2+r1*r3)
    L = ((r2+r3)*w*(a0-1)-r2*a0*w)/(r2+r3)

    zinp = K*(1+I*2*pi*f/C)/(1+I*2*pi*f/L)

    #s = I*2*pi*f
    #Aw = a0/(1+s/w)
    #zinp = (r2 * Aw*(r3+r1) -(Aw-1)*(r2*r3+r1*r2+r1*r3)) / (r2*Aw - (r2+r3)*(Aw-1))
    zinp = simplify(zinp)
    mod = sqrt(re(zinp)**2 + im(zinp)**2)
    phase = tan(im(zinp)/re(zinp))
    plotModule(mod,0)
    plotPhase(phase,0)
    return

def substitute(express, case):
    express = express.subs(w,10)        ##check
    express = express.subs(vcc,15)      ##check
    express = express.subs(a0,100000)        ##check
    express = express.subs(pi,3.14159)
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

def plotModule(express, case):
    freq = np.logspace(1,6,num=100,base = 10)
    ZinpM = []
    if case != 0:
        express = substitute(express,case)
    else:
        express1 = substitute(express,1)
        express2 = substitute(express,2)
        express3 = substitute(express,3)
    text = ""
    if case == 1:
        text = ["Caso 1"]
    elif case == 2:
        text = ["Caso 2"]
    elif case == 3:
        text = ["Caso 3"]
    elif case == 0:
        text = ["Caso 1", "Caso 2", "Caso 3"]
    if case != 0:
        for u in range(0,100):
            ZinpM.append(express.subs(f,freq[u]))
        plt.semilogx(freq,ZinpM)
    else:
        ZinpM1 = []
        ZinpM2 = []
        ZinpM3 = []
        for u in range(0,100):
            ZinpM1.append(express1.subs(f,freq[u]))
            ZinpM2.append(express2.subs(f,freq[u]))
            ZinpM3.append(express3.subs(f,freq[u]))
        plt.semilogx(freq,ZinpM1)
        plt.semilogx(freq,ZinpM2)
        plt.semilogx(freq,ZinpM3)
    plt.legend(text)
    plt.grid(which = "both")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud de Impedancia de entrada (Ohms)")
    plt.show()
    return

def plotPhase(express, case):
    freq = np.logspace(1,6,num=100,base = 10)
    ZinpP = []
    if case != 0:
        express = substitute(express,case)
    else:
        express1 = substitute(express,1)
        express2 = substitute(express,2)
        express3 = substitute(express,3)
    text = ""
    if case == 1:
        text = ["Caso 1"]
    elif case == 2:
        text = ["Caso 2"]
    elif case == 3:
        text = ["Caso 3"]
    elif case == 0:
        text = ["Caso 1", "Caso 2", "Caso 3"]
    if case != 0:
        for u in range(0,100):
            ZinpP.append(express.subs(f,freq[u]) * 180/3.142)
        plt.semilogx(freq,ZinpP)
    else:
        ZinpP1 = []
        ZinpP2 = []
        ZinpP3 = []
        for u in range(0,100):
            ZinpP1.append(express1.subs(f,freq[u])* 180/3.142)
            ZinpP2.append(express2.subs(f,freq[u])* 180/3.142)
            ZinpP3.append(express3.subs(f,freq[u])* 180/3.142)
        plt.semilogx(freq,ZinpP1)
        plt.semilogx(freq,ZinpP2)
        plt.semilogx(freq,ZinpP3)
    plt.legend(text)
    plt.grid(which = "both")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Fase de la impedancia de entrada (°)")
    plt.show()
    return

init_printing()
a0 = Symbol('a0',real = True)
r1 = Symbol('R1',real = True)
r2 = Symbol('R2',real = True)
r3 = Symbol('R3',real = True)
r4 = Symbol('R4',real = True)
w = Symbol('W',real = True)
f = Symbol('f',real = True)
vcc = Symbol('Vcc',real = True)
main()