class Cat:
    age=0
    def __init__(self,name,furcolor):
        self.name=name
        self.__furcolor=furcolor
    def setAge(self,n):
        Cat.age=n  #由於是類屬性，所以可以直接使用類名.屬性，亦可使用self.屬性
    def printInfo(self):
        print(self.name+'\'s info:')
        print(' Age:',self.age)
        print(' Fur color:',self.__furcolor)

Cat1=Cat('Mr.Ball','black')
Cat1.setAge(2)
Cat1.printInfo()
print('-------------------------')
print(Cat1.name)
print(Cat1._Cat__furcolor)
print(Cat1.__furcolor) #輸出“'Cat' object has no attribute '__furcolor'”