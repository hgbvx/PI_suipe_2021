import numpy
import matplotlib.pyplot as plt
import control as co

#Motor
J = 0.0377 # moment of inertia of the rotor kg.m^2
b = 0.006 # motor viscous friction constant N.m.s
Ke = 1.847 # electromotive force constant V/rad/sec
Kt = 1.847 # motor torque constant 0.01 N.m/Amp
K = 1.847 # constants
R = 3.08 # electric resistance
L = 0.066 #electric inductance 0.5 H

# K / JLs^2 + (Lb + RJ)s + Rb + K^2
num = [K]
den = [J*L,L*b+R*J,R*b+K*K]

# CONTROL PACKAGE

G1= co.tf(num,den)
# noinspection PyUnresolvedReferences
t = numpy.linspace(0, 1, 1000) # time (start, stop, X) in sec

t1, y1 = co.step_response(G1,t)


plt.plot(t1,y1)
plt.xlabel('Time [s]')
plt.ylabel('I [A]')
plt.title('Step Response')
plt.grid()

plt.show()

