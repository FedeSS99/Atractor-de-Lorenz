# cython: language_level=3

import cython
cimport cython
import numpy as np
cimport numpy as np

def dXdtCy(np.float64_t x,np.float64_t y,float sig):
    return sig*(y-x)

def dYdtCy(np.float64_t x,np.float64_t y,np.float64_t z,float rho):
    return (rho-z)*x-y

def dZdtCy(np.float64_t x,np.float64_t y,np.float64_t z,float b):
    return x*y-b*z

@cython.boundscheck(False)
@cython.wraparound(False)
def RungeKutta4Cy(np.float64_t[:] x,np.float64_t[:] y,np.float64_t[:] z,float dt, float sigma, float rho, float b):
    cdef int N = x.shape[0]
    cdef int i
    cdef np.float64_t k1,m1,l1, k2,m2,l2, k3,m3,l3 
    
    for i in range(1,N):
        k1 = dt*dXdtCy( x[i-1], y[i-1], sigma )
        m1 = dt*dYdtCy( x[i-1], y[i-1], z[i-1], rho )
        l1 = dt*dZdtCy( x[i-1], y[i-1], z[i-1], b )

        k2 = dt*dXdtCy( x[i-1]+ k1/2.0, y[i-1]+ m1/2.0, sigma )
        m2 = dt*dYdtCy( x[i-1]+ k1/2.0, y[i-1]+ m1/2.0, z[i-1]+ l1/2.0, rho )
        l2 = dt*dZdtCy( x[i-1]+ k1/2.0, y[i-1]+ m1/2.0, z[i-1]+ l1/2.0, b )

        k3 = dt*dXdtCy( x[i-1]+ k2/2.0, y[i-1]+ m2/2.0, sigma )
        m3 = dt*dYdtCy( x[i-1]+ k2/2.0, y[i-1]+ m2/2.0, z[i-1]+ l2/2.0, rho )
        l3 = dt*dZdtCy( x[i-1]+ k2/2.0, y[i-1]+ m2/2.0, z[i-1]+ l2/2.0, b )

        k4 = dt*dXdtCy( x[i-1]+ k3, y[i-1]+ m3, sigma )
        m4 = dt*dYdtCy( x[i-1]+ k3, y[i-1]+ m3, z[i-1]+ l3, rho )
        l4 = dt*dZdtCy( x[i-1]+ k3, y[i-1]+ m3, z[i-1]+ l3, b )

        x[i] = x[i-1] + (k1+k2+k3+k4)/6.0
        y[i] = y[i-1] + (m1+m2+m3+m4)/6.0
        z[i] = z[i-1] + (l1+l2+l3+l4)/6.0
