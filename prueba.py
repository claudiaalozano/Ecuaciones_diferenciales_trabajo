#create a program in python that integrate the 2d harmonic oscillator and represent it in configuration space
#import necessary modules
import numpy as np
import matplotlib.pyplot as plt

#define constants curvatura y masa del cereal
m=1.0
k=1.0

#set up initial conditions
x0=1.0
y0=1.0
vx0=0.0
vy0=0.0

#define time parameters
t0=0.0
tf=100.0
dt=0.001

#set up empty lists to store data
x_data=[x0]
y_data=[y0]
vx_data=[vx0]
vy_data=[vy0]

#integrate the ODE
t=t0
while t<=tf:
    x=x_data[-1]
    y=y_data[-1]
    vx=vx_data[-1]
    vy=vy_data[-1]
    ax=-(k/m)*x
    ay=-(k/m)*y
    x_new=x+vx*dt+0.5*ax*dt**2
    y_new=y+vy*dt+0.5*ay*dt**2
    vx_new=vx+ax*dt
    vy_new=vy+ay*dt
    x_data.append(x_new)
    y_data.append(y_new)
    vx_data.append(vx_new)
    vy_data.append(vy_new)
    t=t+dt

#plot the results in configuration space
plt.plot(x_data,y_data)
plt.xlabel('x')
plt.ylabel('y')
plt.title('2D Harmonic Oscillator in Configuration Space')
plt.show()