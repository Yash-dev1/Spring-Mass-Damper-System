# Single link arm Parameter File
import numpy as np
# import control as cnt
import sys
sys.path.append('..')  # add parent directory
import Param as P

Ts = P.Ts  # sample rate of the controller
sigma = 0.05  # dirty derivative bandwidth is 1/sigma
F_max = P.F_max  # limit on control signal

#  tuning parameters
tr =  1.625 # (calculated from Q8 part b) tuned for fastest possible rise time before saturation.
zeta = 0.707
ki = 0.1  # integrator gain

# desired natural frequency
wn = 2.2/tr
alpha1 = 2.0*zeta*wn
alpha0 = wn**2

# compute PD gains
kp = (alpha0*P.m)-P.k
kd = (alpha1*P.m)-P.b

print('kp: ', kp)
print('ki: ', ki)
print('kd: ', kd)



