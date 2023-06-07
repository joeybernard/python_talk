import numpy as np
from datetime import datetime
import sys
from numba import jit

@jit(fastmath=True,nopython=True)
def rungekutta4(f, y0, t, args=()):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n - 1):
        h = t[i+1] - t[i]
        k1 = f(y[i], t[i], *args)
        k2 = f(y[i] + k1 * h / 2., t[i] + h / 2., *args)
        k3 = f(y[i] + k2 * h / 2., t[i] + h / 2., *args)
        k4 = f(y[i] + k3 * h, t[i] + h, *args)
        y[i+1] = y[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
    return y

@jit(nopython=True,fastmath=True)
def pend(y, t, b, c):
    return np.array([y[1], -b*y[1] - c*np.sin(y[0])])


size = int(sys.argv[1])
starttime = datetime.now()
b = 0.25
c = 5.0
y0 = np.array([np.pi - 0.1, 0.0])
t = np.linspace(0, 10, size+1)

sol = rungekutta4(pend, y0, t, args=(b, c))
endtime = datetime.now()

print("size = ", size)
print(endtime - starttime)
