num=int(input('input:'))
sum=0
for i in range(1,num+1):
    sum=sum+(-1)**(i-1)*i*(i+1)
print(sum)