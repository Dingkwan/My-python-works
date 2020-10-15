def isPalindrome(string):
    flag=True
    for i in range(0,len(string)):
        if string[i]!=string[-1-i]:  flag=False
        break
    return flag


input_string=input('Please enter a string: ')
print(isPalindrome(input_string))