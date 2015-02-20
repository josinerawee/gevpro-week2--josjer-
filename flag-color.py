#!/usr/bin/env python
import sys
from PyQt4 import QtCore, QtGui
from country import Country
from country import Flagcolor

class Widget(QtGui.QWidget):
	"""het werkt wel als je de widget even minimaliseert en dan weer groot maakt, dan verandert de kleur van de vlag"""
	def __init__(self,country,parent=None):
		
		super(Widget,self).__init__(parent)
		
		self.combo = QtGui.QComboBox()
		self.combo.addItems([i.country for i in country])
		grid=QtGui.QGridLayout()
		grid.addWidget(self.combo,1,0)
		self.setLayout(grid)
		self.connect(self.combo, QtCore.SIGNAL("currentIndexChanged(int)"),self.updateUI)
		self.setGeometry(300,300,250,150)
	
		self.show()
		self.country=Country(self)
		
	def paintEvent(self, event):

		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawRectangle(qp)
		qp.end()
        
	def drawRectangle(self, qp):
		qp.setBrush(self.country.color)
		qp.drawRect(10, 10,20,20)	
		
	def updateUI(self):
		self.from_=unicode(self.combo.currentText())
		self.country=Country(self.from_)


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
