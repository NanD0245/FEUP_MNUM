import math

def f(x):
    return math.sin(x)

def trapezios(a,b,n):
    h = (b-a)/n
    soma = 0
    for i in range(n+1):
        if (i==0 or i==n):
            soma += f(a + i*h)
        else:
            soma += 2*f(a + i*h)
    return (h/2)*soma

print("RESULT: \n",trapezios(0, math.pi/2, 80))

error = (trapezios(0,math.pi/2,80) - trapezios(0,math.pi/2,40))/3

print("\nERROR:\n", error)

qc = (trapezios(0,math.pi/2,40) - trapezios(0,math.pi/2,20))/(trapezios(0,math.pi/2,80) - trapezios(0,math.pi/2,40))

print("\nQC:\n", qc)