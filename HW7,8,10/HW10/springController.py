import numpy as np
import springParamHW10 as P
import sys
sys.path.append('..')  # add parent directory
import Param as P0
from PIDControl import PIDControl


class springController:

    def __init__(self):
        # Instantiates the PD object
        self.zCtrl = PIDControl(P.kp, P.ki, P.kd,
                                    P0.F_max, P.sigma, P.Ts)
        self.limit = P0.F_max

    def update(self, z_r, y):
        z = y.item(0)
        #zdot = y.item(1)

         # equilibrium torque around theta_e = 0
        
        #F_e = P0.k*z_e

        # compute the linearized force using PD control
        F_tilde = self.zCtrl.PID(z_r, z, False)

        # compute total torque
        F =F_tilde

        #tau = tau_e + tau_tilde
        # always saturate to protect hardware
        F = self.saturate(F)

        return F

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)

        return u







