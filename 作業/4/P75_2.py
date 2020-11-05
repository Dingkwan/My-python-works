def Whether_prime(input):
    for i in range(2,input):
        if input%i==0:
            return -1
    return input

prime_list=[]
for i in range(100,1000):
    if Whether_prime(i)==i:
        prime_list.append(i)

print(prime_list)