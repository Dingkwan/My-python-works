def multi(*num):
    mul=1
    for i in num:
        mul*=i
    return mul

print('Result:',multi(3,4,2))