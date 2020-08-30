from math import *
import random
#///////////////////////////////////////////////////////////////////////////////////////
#------------------------------------------.....---------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
derivative =lambda f,x,h: (f(x+h)-f(x-h))/(2*h)
#region
#print(derivative(cos,0,0.0001))
#print(derivative(sin,pi,0.0001))
#print(derivative(exp,1,0.0001))
#endregion
#///////////////////////////////////////////////////////////////////////////////////////
#------------------------------------------.....---------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def solve(f,x0,h):
    x = x0
    xn = lambda x,h : x-f(x)/derivative(f,x,h)
    while abs(x-xn(x,h))>h or xn(x,h)==x:
        x = xn(x,h)
    return x
k = lambda x:x**2+2*x+2
#print(solve(cos,0.0002,0.00001))
#print(solve(exp,2,0.00001))
#print(solve(sin,0.0001,0.00001))
