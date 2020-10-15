import math
m=2
print('1')
while m<100:
    j=2
    while j<=math.sqrt(m):
        if m%j==0:break
        j=j+1
    if j>math.sqrt(m):
        print(m)
    m=m+1
