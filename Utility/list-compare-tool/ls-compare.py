#/usr/bin/python3

import csv 
with open('test-set01/from.csv','r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)
