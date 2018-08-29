from cython import parallel, boundscheck
import numpy as np

def convert_fahrenheit(int number):
    cdef float result = 0
    result = number * 1.800 + 32
    return result

@boundscheck(False)
def conv_all(array_me):
    cdef int i
    cdef short [:] var_l = np.array(array_me, np.int16)
    lenght = var_l.shape[0]
    with nogil:
        for i in parallel.prange(lenght, schedule='guided'):
            var_l[i] * 1.8 + 32