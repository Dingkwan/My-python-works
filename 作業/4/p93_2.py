from shutil import copy

with open('copy.txt','w') as file:
    file.write('Oh, my god')

copy('copy.txt','copy1.txt')