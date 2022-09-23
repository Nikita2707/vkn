from cmath import log10
import math 
x=float(input("введіть х"))
def f1(x1):
    rez=math.log1p(math.fabs(x1-1))+log10(math.fabs(x**0.7+2))
    return(rez)
def f2(x2):
    rez=math.e*4*x**7+2-((x2)**1/3)-5.7
    return(rez)
def f3(x3):
    rez=4.27*x+4.33*x3**2+math.sin(x3+1)
    return(rez)
y=0.0
if x > 12.1:
    y=f1(x)
if x > -5.7 and x < 12.1:
    y=f2(x)
if x< -5.7:
    y=f3(x)
print(y)