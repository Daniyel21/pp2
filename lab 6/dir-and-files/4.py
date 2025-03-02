import os
import string

with open("lab 6/dir-and-files/sometext.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()