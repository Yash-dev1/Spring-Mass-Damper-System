import sys
sys.path.append('..')  # add parent directory
import matplotlib.pyplot as plt
import numpy as np
import Param as P
from Dynamics import Dynamics
from Controller11 import Controller
from SignalGenerator import SignalGenerator
from Animation import Animation
from dataPlotter import dataPlotter

# instantiate arm, controller, and reference classes
dynamics = Dynamics()
controller = Controller()
reference = SignalGenerator(amplitude=1,
                            frequency=0.05)
disturbance = SignalGenerator(amplitude=0.25)

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = Animation()

t = P.t_start  # time starts at t_start
y = dynamics.h()  # output of system at start of simulation

while t < P.t_end:  # main simulation loop
    # Get referenced inputs from signal generators
    # Propagate dynamics in between plot samples
    t_next_plot = t + P.t_plot

    # updates control and dynamics at faster simulation rate
    while t < t_next_plot: 
        r = reference.square(t)
        d = disturbance.square(t) # input disturbance
        n = 0.0  #noise.random(t)  # simulate sensor noise
        x = dynamics.state
        u = controller.update(r, x)  # update controller
        y = dynamics.update(u.item(0) + d)  # propagate system
        t = t + P.Ts  # advance time by Ts

    # update animation and data plots
    animation.update(dynamics.state)
    dataPlot.update(t, r, dynamics.state, u)

    # the pause causes the figure to display during simulation
    plt.pause(0.0001)  

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
