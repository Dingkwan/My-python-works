def letters_in_string(string):
    count=0
    for letter in string:
        count+=1
    return count

String=input('请输入字串：')
print('这个字串有',letters_in_string(String),'个字符')