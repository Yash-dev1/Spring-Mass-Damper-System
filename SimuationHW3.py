import matplotlib.pyplot as plt
import sys
sys.path.append('..')  # add parent directory
import Param as P
from SignalGenerator import SignalGenerator
from Animation import Animation
from dataPlotter import dataPlotter
from Dynamics import Dynamics

# instantiate pendulum, controller, and reference classes
spring = Dynamics(alpha=0.02)
reference = SignalGenerator(amplitude=0.7, frequency=0.05)
force = SignalGenerator(amplitude=1, frequency=1)

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = Animation()


t = P.t_start  # time starts at t_start
while t < P.t_end:  # main simulation loop

    # Propagate dynamics at rate Ts
    t_next_plot = t + P.t_plot
    while t < t_next_plot:
        r = reference.square(t)
        u = force.sin(t)
        y = spring.update(u)  # Propagate the dynamics
        t = t + P.Ts  # advance time by Ts

    # update animation and data plots at rate t_plot
    animation.update(spring.state)
    dataPlot.update(t, r, spring.state, u)

    # the pause causes figure to be displayed during simulation
    plt.pause(0.0001)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()