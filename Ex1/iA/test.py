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

def substitute(express, case):
    express = express.subs(w,8* 2 * 3.142)        ##check
    express = express.subs(vcc,15)      ##check
    express = express.subs(a0,100000)        ##check
    #express = express.subs(pi,3.14159)
    express = express.subs(SR,0.5*10**6)
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
vcc = Symbol('Vcc',real = True, positive = True)
SR = Symbol('SR',real = True, positive = True)
Vp = Symbol('Vp',real = True, positive = True)
Vin = Symbol('Vin',real = True, positive = True)

s = Symbol('s')
#s = I*2*3.142*f
Aw = a0 / (1+s/w)

h = (-r2 / r1) * 1 / (1 + 1/Aw - r2/(r3*Aw) + r2/(r1*Aw))
h = simplify(h)
mod = sqrt(re(h)**2 + im(h)**2)
mod = simplify(mod)

'''
temp = SR/(mod * 2 * pi*Vp) - f
temp = simplify(temp)
f = simplify(solve(temp,f))
f = simplify(f[1])
f1 = substitute(f,1)
f1 = simplify(f1)
f2 = substitute(f,2)
f3 = substitute(f,3)

freq = []
Vp1 = []
Vp2 = []
Vp3 = []
for u in range(1,100):
    freq.append(float(u*10**4))
    #Vp1.append(f1.subs(Vp,freq[u-1]))
    #Vp2.append(f2.subs(Vp,freq[u-1]))
    Vp3.append(f3.subs(Vp,freq[u-1]))

plt.semilogx(freq,Vp3)
plt.legend(["Caso 3"])
plt.grid()
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud Pico de entrada")
plt.show()
'''

#print(latex(mod))
#temp1 = substitute(h,1)
#temp2 = substitute(h,2)
#temp3 = substitute(h,3)

'''
temp = mod * Vin - vcc
temp = simplify(temp)
fcr = simplify(solve(temp,Vin))
fcr1=substitute(fcr[0],1)
fcr2=substitute(fcr[0],2)
fcr3=substitute(fcr[0],3)


freq = []
Vp1 = []
Vp2 = []
Vp3 = []
for u in range(0,20):
    freq.append(float((u)*100000))
    Vp1.append(fcr1.subs(f,freq[u]))
    Vp2.append(fcr2.subs(f,freq[u]))
    Vp3.append(fcr3.subs(f,freq[u]))

plt.semilogx(freq,Vp3)
plt.legend(["Caso 3"])
plt.grid()
plt.xlabel("Frecuencia minima")
plt.ylabel("Amplitud de entrada")
plt.show()
'''