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



init_printing()
a0 = Symbol('a0',real = True)
r1 = Symbol('R1',real = True)
r2 = Symbol('R2',real = True)
r3 = Symbol('R3',real = True)
r4 = Symbol('R4',real = True)
w = Symbol('W',real = True)
f = Symbol('f',real = True)
vcc = Symbol('Vcc',real = True)

K = (r2*a0*w*(r3+r1)-w*(a0-1)*(r2*r3+r1*r2+r1*r3)) / (r2*a0*w-(r2+r3)*w*(a0-1))
C = (w*(a0-1)*(r2*r3+r1*r2+r1*r3)-r2*a0*w*(r3+r1))/(r2*r3+r1*r2+r1*r3)
L = ((r2+r3)*w*(a0-1)-r2*a0*w)/(r2+r3)

zinp = K*(1+I*2*pi*f/C)/(1+I*2*pi*f/L)
zinp1 = substitute(zinp,1)
zinp2 = substitute(zinp,2)
zinp3 = substitute(zinp,3)
zinp1 = re(zinp1) + I * im(zinp1)
zinp2 = re(zinp2) + I * im(zinp2)
zinp3 = re(zinp3) + I * im(zinp3)
zinp1 = simplify(zinp1)
zinp2 = simplify(zinp2)
zinp3 = simplify(zinp3)

mod1 = sqrt(re(zinp1)**2+im(zinp1)**2)
mod1 = simplify(mod1)
ph1 = tan(im(zinp1)/re(zinp1))
ph1 = simplify(ph1)

mod2 = sqrt(re(zinp2)**2+im(zinp2)**2)
mod2 = simplify(mod2)
ph2 = tan(im(zinp2)/re(zinp2))
ph2 = simplify(ph2)

mod3 = sqrt(re(zinp3)**2+im(zinp3)**2)
mod3 = simplify(mod3)
ph3 = tan(im(zinp3)/re(zinp3))
ph3 = simplify(ph3)



'''
freq = []
zio1m = []
zio1p = []
zio2m = []
zio2p = []
zio3m = []
zio3p = []

for i in range(0,50):
    freq.append(float(2.71828182**float(i)))
    temp = zinp1.subs(f,freq[i])
    temp = temp.evalf()
    temp2 = sqrt(re(temp.evalf())**2 + im(temp)**2)
    zio1m.append(temp2)
    temp2 = tan(im(temp)/re(temp))
    zio1p.append(temp2)

    temp = zinp2.subs(f,freq[i])
    temp = temp.evalf()
    temp2 = sqrt(re(temp.evalf())**2 + im(temp)**2)
    zio2m.append(temp2)
    temp2 = tan(im(temp)/re(temp))
    zio2p.append(temp2)

    temp = zinp3.subs(f,freq[i])
    temp = temp.evalf()
    temp2 = sqrt(re(temp.evalf())**2 + im(temp)**2)
    zio3m.append(temp2)
    temp2 = tan(im(temp)/re(temp))
    zio3p.append(temp2)

print (freq[10], zio1m[10], zio1p[10])

'''