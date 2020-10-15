import random
x=random.randrange(100,201)
maxn=x
print(x,end=" ")
for i in range(2,11):
    x=random.randrange(100,201)
    print(x,end=" ")
    if x>maxn:
        maxn=x
print("最大数",maxn)