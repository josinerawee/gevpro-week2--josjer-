import sys
from PyQt4 import QtCore, QtGui
from random import randrange


class Country(QtGui.QColor):
	"""Genereert een country object en geeft een random kleur"""
	def __init__(self,country):
		self.country = country
		
	def __str__(self):
		return "Hello from {0}".format(self.country)
		
	def getcolor(self):
		
		self.color=QtGui.QColor(0,0,0)
		self.color.setRed(randrange(0,256))
		self.color.setGreen(randrange(0,256))
		self.color.setBlue(randrange(0,256))
		return self.color
		
def main():
	countryname = Country("Holland")
	print(countryname)

if __name__ == "__main__":
	main()
