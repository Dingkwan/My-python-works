def Low_to_Cap(String):
    return str(String).upper()

def Cap_to_Low(String):
    return str(String).lower()

input_string=input('Please enter a string: ')
print('Capital:',Low_to_Cap(input_string))
print('Lowercase:',Cap_to_Low(input_string))