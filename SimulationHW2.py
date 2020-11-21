import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..') # add parent directory
import Param as P
from SignalGenerator import SignalGenerator
from Animation import Animation
from dataPlotter import dataPlotter

# instatiate reference input classes
reference = SignalGenerator(amplitude=1,frequency=0.5)
zRef = SignalGenerator(amplitude=1, frequency=0.5) 
fRef = SignalGenerator(amplitude=5, frequency=.5) 


# instatiate the simulation plots and Animation
dataPlot = dataPlotter()
animation = Animation()

t = P.t_start  # time starts at t_start
while t < P.t_end:  # main simulation loop
    # set variables
    r = reference.square(t)
    z = zRef.sin(t)
    f = fRef.sawtooth(t)
    # update animation
    state = np.array([[z], [0.0], [0.0]])
    animation.update(state)
    dataPlot.update(t, r, state, f)
    

    t = t + P.t_plot  # advance time by t_plot
    plt.pause(0.05)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
