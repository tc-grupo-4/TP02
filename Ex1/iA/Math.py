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

def substitute(express, case):
    express = express.subs(w,7.5* 2 * 3.142)        ##check
    express = express.subs(vcc,15)      ##check
    express = express.subs(a0,100000)        ##check
    #express = express.subs(pi,3.14159)
    express = express.subs(SR,0.55836*10**6)
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

def slewRate(module, SR, Vin,f):
    eq = SR/(module * 2 * pi*Vin) - f
    eq = simplify(eq)
    VinMaxSR = simplify(solve(eq,Vin))
    VinMaxSR = simplify(VinMaxSR[0])
    return VinMaxSR

def saturation(module,Vin,Vcc):
    eq = module * Vin - vcc 
    VinMaxSat = simplify(solve(eq,Vin))
    VinMaxSat = VinMaxSat[0]
    return VinMaxSat

def plotVinMaxInFreq(express, case):
    freq = np.logspace(1,6,num=100,base = 10)
    VinMax = []
    express = substitute(express,case)
    text = ""
    if case == 1:
        text = "Caso 1"
    elif case == 2:
        text = "Caso 2"
    elif case == 3:
        text = "Caso 3"
    for u in range(0,100):
        VinMax.append(express.subs(f,freq[u]))
    plt.semilogx(freq,VinMax)
    plt.legend([text])
    plt.grid()
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud máxima de entrada (V)")
    plt.show()
    return

def plotVinMaxInFreqTotal(slewRateExpression, saturationExpression,case):
    freq = np.logspace(1,7,num=100,base = 10)
    VinMax = []
    slewRateExpression = substitute(slewRateExpression,case)
    saturationExpression = substitute(saturationExpression,case)
    text = ""
    if case == 1:
        text = "Caso 1"
    elif case == 2:
        text = "Caso 2"
    elif case == 3:
        text = "Caso 3"
    
    for u in range(0,100):
        temp = slewRateExpression.subs(f,freq[u])
        temp2 = saturationExpression.subs(f,freq[u])
        ans = min(temp,temp2)
        VinMax.append(ans)
    plt.semilogx(freq,VinMax)
    plt.legend([text])
    plt.grid(which = "both")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud máxima de entrada (V)")
    plt.show()
    return

init_printing()
a0 = Symbol('a0',real = True, positive = True)
r1 = Symbol('R1',real = True, positive = True)
r2 = Symbol('R2',real = True, positive = True)
r3 = Symbol('R3',real = True, positive = True)
r4 = Symbol('R4',real = True, positive = True)
w = Symbol('W',real = True, positive = True)
f = Symbol('f',real = True, positive = True)
vcc = Symbol('Vcc',real = True, positive = True)
SR = Symbol('SR',real = True, positive = True)
Vp = Symbol('Vp',real = True, positive = True)
Vin = Symbol('Vin',real = True, positive = True)
#s = Symbol('s')

s = I*2*3.142*f
Aw = a0 / (1+s/w)
h = (-r2 / r1) * 1 / (1 + 1/Aw + r2/(r3*Aw) + r2/(r1*Aw))
h = simplify(h)

modH = sqrt(re(h)**2 + im(h)**2)
modH = simplify(modH)

phH = tan(im(h)/re(h)) * 180 / pi
phH = simplify(phH)


expressSat = saturation(modH,Vin,vcc)
expressSR = slewRate(modH,SR,Vin,f) 
plotVinMaxInFreqTotal(expressSR, expressSat, 3)