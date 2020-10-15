for x in range(0,101):
    for y in range(0,101):
        for z in range(0,101):
            if 3*x+2*y+0.5*z==100 and x+y+z==100:
                print('大：',x,'   ','小：',y,'   ','驹：',z)
                print('-----------------------')