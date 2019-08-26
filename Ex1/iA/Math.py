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

def main():
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
    #plotVinMaxInFreq(expressSR,0)
    plotVinMaxInFreqTotal(expressSR, expressSat, 0)

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
    eq = module * Vin - Vcc 
    VinMaxSat = simplify(solve(eq,Vin))
    VinMaxSat = VinMaxSat[0]
    return VinMaxSat

def plotVinMaxInFreq(express, case):
    freq = np.logspace(1,6,num=100,base = 10)
    VinMax = []
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
            VinMax.append(express.subs(f,freq[u]))
        plt.semilogx(freq,VinMax)
    else:
        VinMax1 = []
        VinMax2 = []
        VinMax3 = []
        for u in range(0,100):
            VinMax1.append(express1.subs(f,freq[u]))
            VinMax2.append(express2.subs(f,freq[u]))
            VinMax3.append(express3.subs(f,freq[u]))
        plt.semilogx(freq,VinMax1)
        plt.semilogx(freq,VinMax2)
        plt.semilogx(freq,VinMax3)
    plt.legend(text)
    plt.grid(which = "both")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud máxima de entrada (V)")
    plt.show()
    return

def plotVinMaxInFreqTotal(slewRateExpression, saturationExpression,case):
    freq = np.logspace(1,7,num=100,base = 10)
    VinMax = []
    if case != 0:
        slewRateExpression = substitute(slewRateExpression,case)
        saturationExpression = substitute(saturationExpression,case)
    else:
        slewRateExpression1 = substitute(slewRateExpression,1)
        saturationExpression1 = substitute(saturationExpression,1)
        slewRateExpression2 = substitute(slewRateExpression,2)
        saturationExpression2 = substitute(saturationExpression,2)
        slewRateExpression3 = substitute(slewRateExpression,3)
        saturationExpression3 = substitute(saturationExpression,3)
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
            temp = slewRateExpression.subs(f,freq[u])
            temp2 = saturationExpression.subs(f,freq[u])
            ans = min(temp,temp2)
            VinMax.append(ans)
        plt.semilogx(freq,VinMax)
    else:
        VinMax1 = []
        VinMax2 = []
        VinMax3 = []
        for u in range(0,100):
            temp = slewRateExpression1.subs(f,freq[u])
            temp2 = saturationExpression1.subs(f,freq[u])
            ans = min(temp,temp2)
            VinMax1.append(ans)
            temp = slewRateExpression2.subs(f,freq[u])
            temp2 = saturationExpression2.subs(f,freq[u])
            ans = min(temp,temp2)
            VinMax2.append(ans)
            temp = slewRateExpression3.subs(f,freq[u])
            temp2 = saturationExpression3.subs(f,freq[u])
            ans = min(temp,temp2)
            VinMax3.append(ans)
        plt.semilogx(freq,VinMax1)
        plt.semilogx(freq,VinMax2)
        plt.semilogx(freq,VinMax3)
    plt.legend(text)
    plt.grid(which = "both")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud máxima de entrada (V)")
    plt.show()
    return

main()