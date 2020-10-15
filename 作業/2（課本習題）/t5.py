import random
count=0
sum=0
list=[]
while 1:
    random_num=random.randint(1,15)
    if random_num%2!=0:
        count=count+1
        list.append(random_num)
        if count==10:
            break
print('当前列表：',list)
for i in range(0,len(list)):
    sum=sum+list[i]
print('和：',sum)
print('平均值：',sum/10)