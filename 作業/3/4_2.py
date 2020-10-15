def sum_add(base,time):
    sumlist=[]
    for i in range(1,time+1):
        string_to_int=int(str(base)*i)
        sumlist.append(string_to_int)
    return sum(sumlist)
base=int(input('base:'))
time=int(input('time:'))
print('sum:',sum_add(base,time))