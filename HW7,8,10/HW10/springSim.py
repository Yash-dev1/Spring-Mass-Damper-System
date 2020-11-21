import sys
sys.path.append('..')  # add parent directory
import matplotlib.pyplot as plt
import numpy as np
import Param as P
from springDynamics1 import Dynamics
from springController import springController
from signalGenerator import signalGenerator
from Animation import Animation
from dataPlotter import dataPlotter

# instantiate arm, controller, and reference classes
spring = Dynamics(0.2)
controller = springController()
reference = signalGenerator(amplitude=1, frequency=0.05)#amplitude chosen according to 1 m step input, frequency = wn
disturbance = signalGenerator(amplitude=0.0)

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = Animation()

t = P.t_start  # time starts at t_start
y = spring.h()  # output of system at start of simulation
while t < P.t_end:  # main simulation loop
    # Get referenced inputs from signal generators
    # Propagate dynamics in between plot samples
    t_next_plot = t + P.t_plot

    # updates control and dynamics at faster simulation rate
    while t < t_next_plot: 
        r = reference.square(t)
        d = disturbance.step(t)  # input disturbance
        n = 0.0  #noise.random(t)  # simulate sensor noise
        x = spring.state
        u = controller.update(r,x)  # update controller, instead of state x we have put output y itself
        y = spring.update(u + d)  # propagate system
        t = t + P.Ts  # advance time by Ts

    # update animation and data plots
    animation.update(spring.state)
    dataPlot.update(t, r, spring.state, u)

    # the pause causes the figure to be displayed for simulation
    plt.pause(0.0001)  

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
