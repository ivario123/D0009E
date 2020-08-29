from math import *
import random
derivative =lambda f,x,h: (f(x+h)-f(x-h))/(2*h)
#region
print(derivative(cos,0,0.0001))
print(derivative(sin,pi,0.0001))
print(derivative(exp,1,0.0001))
#endregion
def solve(f,x0,h):
    x = x0
    fx = 0
    while abs(x)-abs(fx) > h or fx==x:
        fx = x
        x = fx-f(fx)/derivative(f,fx,h)
    return x
f = lambda x:pow(x,2)*4+2*x
print(derivative(f,4,0.000001))
print(solve(f,0,0.0001))
