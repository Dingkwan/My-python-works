def cap_and_low_num(string):
    Lowercase=0
    Capital=0
    for letter in string:
        if letter>='a' and letter<='z':
            Lowercase+=1
        if letter>='A' and letter<='Z':
            Capital+=1
    return Capital,Lowercase

string=input('输入字串：')

return_cap,__=cap_and_low_num(string)
__,return_low=cap_and_low_num(string)

print('有',return_cap,'个大写字母')
print('有',return_low,'个小写字母')