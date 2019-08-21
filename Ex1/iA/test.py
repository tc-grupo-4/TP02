from sympy import Symbol
from sympy import Function, simplify
from sympy import *
from sympy import init_printing
from sympy.core.numbers import pi, I, oo
from sympy import re, im
from sympy.solvers.inequalities import solve_rational_inequalities
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy.solvers import solve

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

h = ((a0*r3*r2)/(r1*r2+2*r3*r1-r3*r2)) / (1+ (I*2*pi*f)/w*((r1*r2+2*r3*r1-r3*r2)/(r1*r2+r3*r1-r3*r2)))
h = simplify(h)

mod = sqrt(re(h)**2 + im(h)**2)
mod = simplify(mod)

temp1 = substitute(h,1)
temp2 = substitute(h,2)
temp3 = substitute(h,3)

print(latex(temp3))

#print(latex(simplify(solve(mod-vcc,f))))
#fcr = simplify(solve(mod-vcc,f))
#fcr=substitute(fcr[1],3)
#print(fcr.evalf())