def fac(n):
    if n==1:p=1
    else:p=fac(n-1)*n
    return p
x=int(input('输入一个正整数：'))
print(fac(x))