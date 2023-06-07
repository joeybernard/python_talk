import numpy as np
from scipy.integrate import solve_ivp
from datetime import datetime
import sys


def pend(t, y):
    return (-0.25*t - 5.0*np.sin(y))


size = int(sys.argv[1])
starttime = datetime.now()
b = 0.25
c = 5.0
#y0 = np.array([np.pi - 0.1, 0.0])
y0 = [1]
t0 = 0
tf = 10
t = np.linspace(t0, tf, size)

sol = solve_ivp(fun=pend, t_span=[t0,tf], y0=y0, t_eval=t)
endtime = datetime.now()

print("size = ", size)
print(endtime - starttime)
