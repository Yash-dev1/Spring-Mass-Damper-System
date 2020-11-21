# Single link arm Parameter File
import numpy as np
# import control as cnt
import sys
sys.path.append('..')  # add parent directory
import Param as P

Ts = P.Ts  # sample rate of the controller
beta = P.beta  # dirty derivative gain
F_max = P.F_max  # limit on control signal

#  tuning parameters
#tr = 2 #for part a
tr = 1.625 # (for part b) tuned to get fastest possible rise time before saturation.

zeta = 0.7

# desired natural frequency
wn = 2.2/tr
alpha1 = 2.0*zeta*wn
alpha0 = wn**2

# compute PD gains
kp = wn**2*P.m - P.k   
kd = P.m*2*wn *zeta - P.b  

print('kp: ', kp)
print('kd: ', kd)
