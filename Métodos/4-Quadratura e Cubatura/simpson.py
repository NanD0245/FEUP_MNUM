import math

def f(x):
    return math.sin(x)

def simpson(a,b,n):
    h = (a+b)/n
    soma = 0
    for i in range(n+1):
        if (i == 0 or i == n):
            soma += f(a+i*h)
        elif (i%2 == 1):
            soma += 4*f(a+i*h)
        else:
            soma += 2*f(a+i*h)
    return (h/3)*soma

print("RESULT: \n",simpson(0, math.pi/2, 80))

error = (simpson(0,math.pi/2,80) - simpson(0,math.pi/2,40))/15

print("\nERROR:\n", error)

qc = (simpson(0,math.pi/2,40) - simpson(0,math.pi/2,20))/(simpson(0,math.pi/2,80) - simpson(0,math.pi/2,40))

print("\nQC:\n", qc)
