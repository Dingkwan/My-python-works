def over_1000():
    count=1
    sum=0
    while sum<1000:
        sum=sum+count*count
        count+=1
    return count

print(over_1000())