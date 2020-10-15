num=input('input:')
num_copy=int(num)
num_add=1
sum=0
while num_add!=int(num)+1:
    sum=sum+(num_copy*num_add)
    num_add=num_add+1
    num_copy=num_copy-1
print(sum)