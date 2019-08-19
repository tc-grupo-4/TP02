from sympy import Symbol
from sympy import Function, simplify
from sympy import *
from sympy import init_printing
from sympy.core.numbers import pi, I, oo
from sympy import re, im
from sympy.solvers.inequalities import solve_rational_inequalities
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy.solvers import solve
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

print(latex(simplify(solve(mod-vcc,f))))
