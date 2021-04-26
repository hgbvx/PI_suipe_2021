import numpy
import matplotlib.pyplot as plt
import control as co
from SUiPE import Simulation

#Motor
motor_parameters = {
"J" : 0.0377,        # moment of inertia of the rotor kg.m^2
"b" : 0.006,         # motor viscous friction constant N.m.s
"K" : 1.847,         # torque/electromotive force constant
"R" : 3.08,          # electric resistance
"L" : 0.066         #electric inductance 0.5 H
}
#Simulation parameters
n = 1000     # nr of samples
start = 0    # Start of simulation [s]
stop = 10    # Stop of simulation  [s]

# noinspection PyUnresolvedReferences
# Time of simulation and number of samples
t = numpy.linspace(start, stop, n) # time (start, stop, X) in sec

#Simulation blocks
block1 = Simulation.PI(kp=4.7, ti=1.8118)                  # PI regulator
block2 = Simulation.motor_tf(motor_parameters)             # Motor transfer function without kfi and inertia
block3 = Simulation.kfi(motor_parameters)                  # Kfi
block4 = Simulation.inertia_integrator(motor_parameters)   # Inertia
block5 = Simulation.noise(mean=0,var= 0.001, samples= n)   # Noise
#Connecting blocks
main_block = block1*block2*block3*block4

#Creating feedback
final = co.feedback(main_block,1,-1) #feedback

#Step response
t1, y1 = co.step_response(final,t)


plt.plot(t1,y1)
plt.xlabel('Time [s]')
plt.ylabel('I [A]')
plt.title('Step Response')
plt.grid()

plt.show()

