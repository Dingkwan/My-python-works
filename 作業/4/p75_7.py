def pyramid(n,row):
    for i in range(0,row):
        print(' '*(row-1-i)+n*(2*i+1))

input_n=input('Input the character you want to see:')
input_row=int(input('Input the number of the rows you want to display:'))
pyramid(input_n,input_row)