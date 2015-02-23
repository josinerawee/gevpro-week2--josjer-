#!/usr/bin/env python
import sys
from PyQt4 import QtCore, QtGui
from country import Country

class Widget(QtGui.QWidget):
	"""Maakt een scherm met een dropdown menu en een vlag. Als je een land aanklikt, laat hij de bijbehorende vlag hierbij zien."""
	def __init__(self,country,parent=None):
		
		super(Widget,self).__init__(parent)
		self.initUI(country)
		
	def initUI(self,country):
		
		self.country=Country(self)
		self.color=self.country.getcolor()
		self.colorname = self.color.name()
		self.countrycolors = {}
		self.countrycolors[self.country] = self.colorname	
		self.combo = QtGui.QComboBox()
		self.combo.addItems([i.country for i in country])
		self.square = QtGui.QFrame(self)
		self.square.setStyleSheet("QWidget { background-color: %s }" % self.color.name())
		grid=QtGui.QGridLayout()
		grid.addWidget(self.square,2,0)
		grid.addWidget(self.combo,1,0)
		self.setLayout(grid)
		self.connect(self.combo, QtCore.SIGNAL("currentIndexChanged(int)"),self.updateUI)
		self.setGeometry(300,300,250,150)
		self.show()

		
	def updateUI(self):
		self.from_=unicode(self.combo.currentText())
		if self.from_ not in self.countrycolors:
			self.color=self.country.getcolor()
			self.colorname = self.color.name()
			self.countrycolors[self.from_] = self.colorname
		self.square.setStyleSheet("QFrame { background-color: %s }" % self.countrycolors[self.from_])

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
