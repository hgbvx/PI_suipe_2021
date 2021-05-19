import control as co
import numpy as np


class Simulation:

	@staticmethod
	def pi(kp, ti):
		"""

		:param kp: Gain of regulator
		:param ti: Inertia of regulator
		:return: Transfer function of PI
		"""
		tf1 = co.tf([kp], [1])
		tf2 = co.tf([1], [ti, 0])
		tf3 = tf1 * tf2
		return tf1 + tf3

	@staticmethod
	def motor_tf(parameters):  # K / JLs^2 + (Lb + RJ)s + Rb + K^2
		"""

		:param parameters: Dictionary with resistance and inductance of motor
		:return: Transfer function of motor
		"""
		resistance = parameters["R"]
		inductance = parameters["L"]
		return co.tf([1], [inductance, resistance])

	@staticmethod
	def kfi(parameters):
		"""

		:param parameters: Dictionary with Kfi
		:return: Transfer function of Kfi
		"""
		kfi = parameters["K"]
		return co.tf([kfi], [1])

	@staticmethod
	def inertia_integrator(parameters):
		"""

		:param parameters: Dictionary with moment of inertia
		:return: Transfer function of inertia integrator
		"""
		inertia = parameters["J"]
		return co.tf([1], [inertia, 0])

	@staticmethod
	# TODO: transfer function
	def noise(mean, var, samples):
		return np.random.normal(mean, np.sqrt(var), samples)
