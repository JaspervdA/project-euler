import math

A = range(1000)
B = range(1000)

for a in A:
    for b in B:
        c = math.sqrt(a**2+b**2)
        if a + b + c == 1000:
            print(a,b,c)
            print(a*b*c)
