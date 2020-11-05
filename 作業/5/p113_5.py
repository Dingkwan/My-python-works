class person(object):
    def __init__(self, name, age):
        self.name=name
        self.age=int(age)
    
    def setname(self, string):
        self.name=string
    
    def setage(self, num):
        self.age=num

class admin(person):
    typename='Administrator'
    def __init__(self, name, age, worknum, payment):
        super(admin, self).__init__(name, age)
        self.worknum=worknum
        self.payment=int(payment)
    
    def setworknum(self, num):
        self.worknum=num
    
    def setpayment(self, num):
        self.payment=num
    
    def gettype(self):
        return self.typename

    def printInfo(self):
        print('----------------')
        print('Name:',self.name)
        print('Age:',self.age)
        print('Work number:',self.worknum)
        print('Payment:',self.payment)
        print('Type:',self.gettype())
        print('----------------')

class student(person):
    typename='Student'
    def __init__(self, name, age, stunum, borrowbook, borrowbook_date):  #date's format: mm.dd
        super(student, self).__init__(name,age)
        self.stunum=stunum
        self.borrowbook=borrowbook
        self.borrowbook_date=borrowbook_date

    def setstunum(self, num):
        self.stunum=num
    
    def setborrowbook(self, string):
        self.borrowbook=string
    
    def setborrowbook_date(self, string):
        self.borrowbook_date=string

    def gettype(self):
        return self.typename
    
    def printInfo(self):
        print('----------------')
        print('Name:',self.name)
        print('Age:',self.age)
        print('Student number:',self.stunum)
        print('Borrowed book:',self.borrowbook_date)
        print('Date of borrowing book:',self.borrowbook_date)
        print('Type:',self.gettype())
        print('----------------')

ball=admin(name='Mr.Ball', age=10, worknum='01', payment=100)
fur=student(name='Mr.Fur', age=8, stunum='02', borrowbook='Python', borrowbook_date='11.23')

ball.printInfo()
fur.printInfo()

fur.setborrowbook('Web')
print(fur.borrowbook)
print('----------------')
ball.setpayment('200')
print(ball.payment)