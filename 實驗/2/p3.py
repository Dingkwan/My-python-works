a=1
b=1
while a<=9:
    b=1
    while b<=a:
        print(a,'*',b,'=',a*b,end='\t')
        b=b+1
    print("")
    a=a+1