from numba import jit
from math import *
from datetime import datetime
import sys

@jit(nopython=True)
def calc_1(size):
    a = range(size)
    b = []
    for val in a:
        b.append(asin(sin(acos(cos(atan(tan(val)))))) * val)


size = int(sys.argv[1])
starttime = datetime.now()
calc_1(size)
endtime = datetime.now()
print("size = ",size)
print(endtime - starttime)
