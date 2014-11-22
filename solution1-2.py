#!/usr/bin/python
"""
Solution to exercise 2 from lecture 1.
"""


Cn = 1                  # first Catalan number
n = 1                   # counter
Cstop = int(1e6)        # at which value to stop


print 'Catalan numbers not greater than {}:'.format(Cstop)
while Cn <= Cstop:      # continue until Cstop is reached
    print 'C_{{{}}} = {}'.format(n,Cn)
    Cnew = (4 * n + 2) * Cn / (n + 2)
    Cn = Cnew
    n += 1
