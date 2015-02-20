import sys
from PyQt4 import QtCore, QtGui
from random import randrange


class Country:
	
	def __init__(self,country):
		self.country = country
		flag=Flagcolor()
		self.color=flag.getcolor()
	def __str__(self):
		return "Hello from {0}".format(self.country)
	
		
class Flagcolor(QtGui.QColor):
	def __init__(self):
		self.color=QtGui.QColor()
		
	def getcolor(self):
		
		self.color=QtGui.QColor()
		self.color.setRed(randrange(0,256))
		self.color.setGreen(randrange(0,256))
		self.color.setBlue(randrange(0,256))
		return self.color
		
		
def main():
	countryname = Country("Holland")
	print(countryname)

if __name__ == "__main__":
	main()
