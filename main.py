from simple_pid import PID
from scipy import signal
import matplotlib.pyplot as plt

pid = PID(1, 0.1, 0.05, setpoint=1)


#Motor
J = 0.0377 # moment of inertia of the rotor kg.m^2
b = 0.006 # motor viscous friction constant N.m.s
Ke = 0.01 # electromotive force constant V/rad/sec
Kt = 0.01 # motor torque constant 0.01 N.m/Amp
K = 1.847
R = 3.08 # electric resistance
L = 0.066 #electric inductance 0.5 H

# K / JLs^2 + (Lb + RJ)s + Rb + K^2

# Transfer function and setpoint
lti = signal.lti([K], [J*L,L*b+R*J,R*b+K*K])
t, y  = signal.step(lti)
y = y * 1000


plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Speed')
plt.title('Step Response')
plt.grid()

plt.show()