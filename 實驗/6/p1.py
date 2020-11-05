class person(object):
	def __init__(self, name='NULL', sex='NULL', age='NULL'):
		self.name=name
		self.sex=sex
		self.age=age
	
	def printInfo(self):
		print("Name:",self.name)
		print("Sex:",self.sex)
		print("Age:",self.age)
	
	def setName(self,setname):
		self.name=setname
	
	def setSex(self, setsex):
		self.sex=setsex
	
	def setAge(self, setage):
		self.age=setage

class student(person):
	def __init__(self, name='NULL', sex='NULL', age='NULL', stuNum='0000'):
		super(student, self).__init__(name, sex ,age)
		self.stuNum=stuNum
	
	def setstuNum(self, setNum):
		self.stuNum=setNum
	
	def printStuInfo(self):
		print('Name:', self.name)
		print("Sex:", self.sex)
		print("Age:", self.age)
		print('Student Number:', self.stuNum)

mrball=student('Mr.Ball','M','10','1234')
mrball.printStuInfo()
print('---------------------------')
# 修改Mr.Ball的年齡和學號
mrball.setAge('12')
mrball.setstuNum('4321')
mrball.printStuInfo()