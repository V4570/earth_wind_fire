import numpy as np 





class Process():
	def __init__(self):
		print (" Do your magic things")

	def dataProcess(self):


		return None


	def _energyWind(self, p, u):
				"""
			Cp = 
			p = air densirty 
			u = air speed
		"""
		return 0,5*p*(u^3)

	def _energyWaves(self, Cp, p, u):
		"""
			Cp = 
			p = water densirty 
			u = waves speed
		"""
		return 0,5*Cp*p*(u^3)
