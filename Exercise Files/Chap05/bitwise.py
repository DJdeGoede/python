#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 0xef
y = 0x02

z = x & y  # and
q = x | y  # or
r = x ^ y  # xor
s = x << y # shift left
t = x >> y # shift right

print('AND')
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
print(f'(dec) x is {x:02d}, y is {y:02d}, z is {z:02d}')
print ('\nOR')
print(f'(bin) x is {x:08b}, y is {y:08b}, q is {q:08b}')
print(f'(dec) x is {x:02d}, y is {y:02d}, q is {q:02d}')
print ('\nXOR')
print(f'(bin) x is {x:08b}, y is {y:08b}, r is {r:08b}')
print(f'(dec) x is {x:02d}, y is {y:02d}, r is {r:02d}')
print ('\nShift left')
print(f'(bin) x is {x:08b}, y is {y:08b}, s is {s:08b}')
print(f'(dec) x is {x:02d}, y is {y:02d}, s is {s:02d}')
print ('\nShift right')
print(f'(bin) x is {x:08b}, y is {y:08b}, t is {t:08b}')
print(f'(dec) x is {x:02d}, y is {y:02d}, t is {t:02d}')