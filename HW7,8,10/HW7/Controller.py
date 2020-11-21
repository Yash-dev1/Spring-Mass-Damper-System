import numpy as np
import ParamHW7 as P
import sys
sys.path.append('..') # add parent directory
import Param as P0

class Controller:
    def __init__(self):

        # Instantiates the PD object
        self.kp = P.kp
        self.kd = P.kd
        self.limit = P0.F_max

    def update(self, Z_r, x):
        Z = x.item(0)
        Zdot = x.item(1)
        # equilibrium torque around Z_e = 0
        Z_e = 0.0
        F_e = P0.k*Z_e

        # compute the linearized torque using PD control
        F_tilde = self.kp * (Z_r - Z) - self.kd * Zdot

        # compute total torque
        F = F_e + F_tilde

        #tau = tau_e + tau_tilde
        # always saturate to protect hardware
        F = self.saturate(F)

        return F

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u