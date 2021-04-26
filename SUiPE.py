import control as co
import numpy as np

class Simulation:

	@staticmethod
	def PI(kp, ti):
		tf1 = co.tf([kp],[1])
		tf2 = co.tf([1],[ti, 0])
		tf3 = tf1 * tf2
		return tf1 + tf3

	@staticmethod
	def motor_tf(parameters): # K / JLs^2 + (Lb + RJ)s + Rb + K^2
		J = parameters["J"]
		b = parameters["b"]
		Kfi = parameters["K"]
		R = parameters["R"]
		L = parameters["L"]
		return co.tf([1,0],[L, (L*b+R*J)/J, (R*b+Kfi*Kfi)/J])

	@staticmethod
	def kfi(parameters):
		Kfi = parameters["K"]
		return co.tf([Kfi],[1])

	@staticmethod
	def inertia_integrator(parameters):
		J = parameters["J"]
		return co.tf([1],[J,0])

	@staticmethod
	def noise(mean,var,samples):
		return np.random.normal(mean,np.sqrt(var),samples)

