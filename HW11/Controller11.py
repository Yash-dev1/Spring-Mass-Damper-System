import numpy as np
import ParamHW11 as P

class Controller:
    # dirty derivatives to estimate thetadot
    def __init__(self):
        self.K = P.K  # state feedback gain
        self.kr = P.kr  # Input gain
        self.limit = P.F_max  # Maxiumum force
        self.Ts = P.Ts  # sample rate of controller

    def update(self, z_r, x):
        z = x.item(0)
        zdot = x.item(1)

        # Compute the state feedback controller
        F_tilde = -self.K @ x + self.kr * z_r

        # compute total torque
        F = self.saturate(F_tilde)
        return F

    def saturate(self,u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)

        return u
