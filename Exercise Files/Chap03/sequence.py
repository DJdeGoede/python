#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# sequence: always start at 0 so x[2] is the 3rd item

x = [ 1, 2, 3, 4, 5 ]   # list (you can change the values)
y = ( 1, 2, 3, 4, 5 )   # tuple (read only / immutable)

# ranges (also immutable/read only)
z = range(6)            # just 0 to 5
q = range(5, 52, 2)     # from 5 to 50 with steps of 2

# to make a range mutable just make it into a list:
q = list(range(5, 52, 2))
# now you can edit a value like: q[2]=42
# q[2]=42 on the range would give an error!

x[2] = 42
for i in x:
    print('i is {}'.format(i))
print()    
# y[3] = 42   # would give error because value cannot be changed

# range starts with 0, so output will be 0 to 5(six numbers)
for i in z:
    print('i is {}'.format(i))

print()

# from 5 to 50 with steps of 2, last number will be 49
print ('Range: ', end="")
for i in q:
    print('{}'.format(i),end=" ")

print()    
# dictionary (mutable)
x = { 'KEY1': 9.4, 'KEY2': 4, 'KEY3': '17', 'KEY4': True, 'KEY5': None} 
for k, v in x.items():
    print('Key {} has value {}'.format(k, v))


    
    