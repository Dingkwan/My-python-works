class student:
    def __init__(self, stunum='000', name='NULL', birth='NULL'):
        self.stunum=stunum
        self.name=name
        self.birth=int(birth)
    
    def countbirth(self, year):  #year是當前年份
        return year-self.birth

ball=student('123', 'Mr.ball', '1999')
print(ball.name+'\'s age:',ball.countbirth(2020))