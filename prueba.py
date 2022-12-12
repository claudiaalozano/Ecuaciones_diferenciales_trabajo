#create a program in python that integrate the armonic oscillator and represent it's graph

import numpy as np
import matplotlib.pyplot as plt

# integration step
dt = 0.01

# initial conditions
x0 = 0
v0 = 1

# total time
t_max = 10

# time array from 0 to t_max
t_array = np.arange(0, t_max, dt)

# Arrays for storing the values of x and v
x_array = np.zeros(t_array.shape)
v_array = np.zeros(t_array.shape)

# initial values
x_array[0] = x0
v_array[0] = v0

# integration loop
for i in range(1, t_array.size):
    # calculate acceleration
    a = -x_array[i-1]
    
    # calculate velocity
    v_array[i] = v_array[i-1] + a*dt
    
    # calculate position
    x_array[i] = x_array[i-1] + v_array[i]*dt

# plot
plt.plot(t_array, x_array, label='position')
plt.plot(t_array, v_array, label='velocity')
plt.xlabel('time')
plt.ylabel('x')
plt.legend()
plt.show()