import math
x=float(input("введіть x"))
y=((math.cos(x) + math.log1p(math.fabs(x) + 1))/((math.pow(math.e, 0.7 * x)) + math.pow(4, 3.3 * x + 1)) - math.pow(0.9 * x, math.sqrt(2*x)))
print(y)