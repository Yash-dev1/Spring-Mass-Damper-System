import numpy as np

#physical parameters for the mass spring damper system
m = 4.537#4.8 # mass of block, kg
k = 2.631#2.8 # spring constant, N/m
b = 0.452#0.48 # damping constant, Nm/s

# parameters for animation
w = 1 # width of the block, m
h = 1 # height of the block, m
gap = 0.005 # gap between block and x-axis
wall = -2 # position of wall

# initial Conditions
z0 = 2 # initial position of block, m
zdot0 = 0 # initial value of velocity, m/s

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 100  # End time of simulation
Ts = 0.01 # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

# Saturation limit of force
F_max = 5 # , N
