def russian(a, b):
    x = a; y = b
    z = 0
    while x > 0:                           #russian(20, 7)
        if x % 2 == 1: z = z + y           #       x   y  z
        y = y << 1 # doubles y             #       20  7  0  first loop x is even
        x = x >> 1 # halfs x
    return z

print(russian(10, 3))
print(russian(14, 11))

'''Bit shifts 
    17 >> 1
    17 in base 2 is 10001
    10001 >> 1 shifts one position right 
    1000 = 8 in dec
'''