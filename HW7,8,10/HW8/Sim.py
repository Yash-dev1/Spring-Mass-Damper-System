import sys
sys.path.append('..') # add parent directory
import matplotlib.pyplot as plt
import numpy as np
import Param as P
from Dynamics import Dynamics
from Controller import Controller
from SignalGenerator import SignalGenerator
from Animation import Animation
from dataPlotter import dataPlotter

# instantiate arm, controller, and reference classes
D = Dynamics()
controller = Controller()
reference = SignalGenerator(amplitude= 1, frequency=0.05)
disturbance = SignalGenerator(amplitude=0.0)

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = Animation()

t = P.t_start # time starts at t_start

while t < P.t_end:  # main simulation loop
    # Get referenced inputs from signal generators
    # Propagate ynamics in between plot samples
    t_next_plot = t + P.t_plot

    # updates control and dynamics at faster simulation rate
    while t < t_next_plot: 
        r = reference.square(t)
        d = disturbance.step(t)  # input disturbance
        n = 0.0  #noise.random(t)  # simulate sensor noise
        x = D.state
        u = controller.update(r, x)  # update controller
        y = D.update(u + d)  # propagate system
        t = t + P.Ts  # advance time by Ts

    # update animation and data plots
    animation.update(D.state)
    dataPlot.update(t, r, D.state, u)

    # the pause causes the figure to be displayed for simulation
    plt.pause(0.0001)  

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
