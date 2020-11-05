class good(object):
	market='Guangzhou'

	def __init__(self, name='NULL',price='0', madein='NULL', year='1970'):
		self.price=price
		self.madein=madein
		self.year=year

	def printInfo(self):
		print('Price:', self.price)
		print('Made by:', self.madein)
		print('Year:',self.year)
	
	def setYear(self, setyear):
		self.year=setyear

	@staticmethod
	def getMarket():
		print('Market location:',good.market)
	
Ball=good('Ball','30','Poland','2020')
Ball.printInfo()
good.getMarket() #調用靜態方法