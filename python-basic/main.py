#!/usr/bin/python

import os
sep = os.sep
path = os.getcwd()
x = open(f"{path}{sep}files{sep}mbox-short.txt")
count = 0
for line in x:
    print("# Line ",count+1,"#")
    print(line)
    count = count+1

print("Line count: ",count)