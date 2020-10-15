def hcf(x,y):
    if x<y:small=x
    else:small=y
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            count=i
    return count

input1=int(input('input1:'))
input2=int(input('input2:'))
print('最大公约数：',hcf(input1,input2))

