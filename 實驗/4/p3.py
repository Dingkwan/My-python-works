import csv

with open('WHO-COVID-19-global-data.csv','r') as csv_file:
    read_line=csv.reader(csv_file)
    for line in read_line:
        print(line)