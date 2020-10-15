import random
count=0
random_num=random.randint(0,100)
print('随机数已生成')
print(random_num)
while 1:
	input_num=input('输入一个数字：')
	if int(input_num)>int(random_num):
		print('你猜的数比随机数大')
		count=count+1
	elif int(input_num)<int(random_num):
		print('你猜的数比随机数小')
		count=count+1
	elif int(input_num)==int(random_num):
		count=count+1
		print('你答对了，程序结束，你总共用了',count,'次机会')
		break