import numpy as np
import Param as p

class Dynamics:
    def __init__(self, alpha=0.0):
        # Initial state conditions
        y0 = 0.0
        ydot0 = 0.0
        self.state = np.array([
        [y0], # initial condition for y
        [ydot0], # initial condition for ydot
        ])
        self.Ts = p.Ts # simulation time step
        self.limit = p.F_max # input saturation limit
        # system parameters
        self.a0 = (p.k/p.m)
        self.a1 = (p.b/p.m)
        self.b0 = (1/p.m)
        # modify the system parameters by random value
         # Uncertainty parameter
        self.a1 = self.a1 * (1.+alpha*(2.*np.random.rand()-1.))
        self.a0 = self.a0 * (1.+alpha*(2.*np.random.rand()-1.))
        self.b0 = self.b0 * (1.+alpha*(2.*np.random.rand()-1.))

    def f(self, state, u):
        # for system xdot = f(x,u), return f(x,u)
        y = state.item(0)
        ydot = state.item(1)
        # The equations of motion.
        yddot = -self.a1 * ydot - self.a0 * y + self.b0 * u
        # build xdot and return
        xdot = np.array([[ydot], [yddot]])
        return xdot
    def h(self):
        # Returns the measured output y = h(x)
        y = self.state.item(0)
        # return output
        return y

    def update(self, u):
        # This is the external method that takes the input u(t)
        # and returns the output y(t).
        u = self.saturate(u, self.limit) # saturate the input
        self.rk4_step(u) # propagate the state by one time step
        y = self.h() # compute the output at the current state
        return y

    def rk4_step(self, u):
        # Integrate ODE using Runge-Kutta RK4 algorithm
        F1 = self.f(self.state, u)
        F2 = self.f(self.state + self.Ts / 2 * F1, u)
        F3 = self.f(self.state + self.Ts / 2 * F2, u)
        F4 = self.f(self.state + self.Ts * F3, u)
        self.state += self.Ts / 6 * (F1 + 2 * F2 + 2 * F3 + F4)

    def saturate(self, u, limit):
        if abs(u) > limit:
            u = limit*np.sign(u)
        return u