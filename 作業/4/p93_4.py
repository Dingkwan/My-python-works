Cap=0
Low=0
Num=0
Other=0
with open('test.txt','r') as readfile:
    line=readfile.read()

for letter in line:
    if letter>='A' and letter<='Z':
        Cap+=1
    elif letter>='a' and letter<='z':
        Low+=1
    elif letter>='0' and letter<='9':
        Num+=1
    else:
        Other+=1

print('Capital:',Cap)
print('Lowercase:',Low)
print('Number:',Num)
print('Other:',Other)