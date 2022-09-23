import math 
def func(x, y, z):
        R=float((0.7 * math.cos(x) + math.log1p(math.fabs(y)) ** 1/5)) + math.pow(math.e, z+x) 
        return(R)
x1=float(input("введіть x:"))
y1=float(input("введіть y:"))
z1=float(input("введіть z:"))
F=func(x1, y1, z1)
print(F)