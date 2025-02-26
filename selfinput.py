#Output of decrypt.py below

'''
#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1
'''
# Below code is python 2 code converted to python 3
chars = "".join(plaintext) # from previous decrypt.py
b = 1
for i in range(len(chars)):
    if i == (b * b * b):
        print (chars[i])
        b += 1      
#Output will be adlibs
