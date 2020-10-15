list=[1,2,3]
while max(list)<=1200:
    sum=(list[-1]+list[-2]+list[-3])/2
    list.append(sum)
print('第',len(list),'项')