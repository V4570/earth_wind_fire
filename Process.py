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

	def smthng(s):
		min1=s[0][0]
		max1=s[0][0]
		min2=s[0][1]
		max2=s[0][1]
		for i in s:
			if i[0]>max1:
				max1=i[0]
			elif i[0]<min1:
				min1=i[0]

			if i[1]>max2:
				max2=i[1]
			elif i[1]<min2:
				min2=i[1]
		x=max1-min1
		y=max2-min2
		teliko=[]
		for i in range(x):
			for j in range(y):
				teliko.append([0,0])
		for i in s:
				teliko[i[0]-x][i[1]-y].append(i)
