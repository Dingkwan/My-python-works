class good(object):
	def __init__(self, name='NULL',price='0', madeby='NULL', year='1970'):
		self.price=price
		self.madeby=madeby
		self.year=year

	def printInfo(self):
		print('Price:', self.price)
		print('Made by:', self.madeby)
		print('Year:',self.year)
	
	def setPrice(self, setprice):
		self.price=setprice
	
	def setMadeby(self, setmadeby):
		self.madeby=setmadeby
	
	def setYear(self, setyear):
		self.year=setyear

Ball=good('Ball','30','Poland','2020')
Ball.printInfo()
print('----------------')
Ball.setPrice('500')
Ball.printInfo()