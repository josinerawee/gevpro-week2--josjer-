#!/usr/bin/env python
import sys
from PyQt4 import QtCore, QtGui
from random import randrange
class Country:
	def __init__(self,country):
		self.country=country
		
class Widget(QtGui.QWidget):
	def __init__(self,country,parent=None):
		
		super(Widget,self).__init__(parent)
		
		
	
		label = QtGui.QLabel(self)
		self.combo = QtGui.QComboBox()
		self.combo.addItems([i.country for i in country])
		self.color=FlagColor()
		
		grid=QtGui.QGridLayout()
		grid.addWidget(self.combo,1,0)
		self.setLayout(grid)
		self.show()
		
class Flagcolor(QtGui.QColor):
	def __init__(self):
		self.color=QtGui.QColor()
		self.color.setRed(randrange(0,256))
		self.color.setGreen(randrange(0,256))
		self.color.setBlue(randrange(0,256))
		return self.color
		

def getcountries():
	countries = []
	with open('countries_list.txt', 'r') as in_f:
		for line in in_f:
			goed=line.split("\n")
			countries.append(Country(goed[0]))
	return countries

def main():
	app = QtGui.QApplication(sys.argv)
	countries = getcountries()
	ex = Widget(countries)
	sys.exit(app.exec_())
	
	
main()
