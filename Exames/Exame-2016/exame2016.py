import math
# 2

def f2(x,y):
    return x**2 - y - 1.2

def dfx(x,y):
    return 2*x

def dfy(x,y):
    return -1

def g2(x,y):
    return -x + y**2 - 1

def dgx(x,y):
    return -1

def dgy(x,y):
    return 2*y

def newton(x,y):
    print(0,x,y)
    for i in range(5):
        x0 = x
        y0 = y
        x = x0 - ((f2(x0,y0)*dgy(x0,y0) - g2(x0,y0)*dfy(x0, y0)) / (dfx(x0, y0)*dgy(x0, y0) - dgx(x0, y0)*dfy(x0, y0)))
        y = y0 - ((g2(x0,y0)*dfx(x0,y0) - f2(x0,y0)*dgx(x0, y0)) / (dfx(x0, y0)*dgy(x0, y0) - dgx(x0, y0)*dfy(x0, y0))) 
        print(i+1,x,y)
        
# newton(1,1)

# 2.133333     2.066667
# 1.745801     1.697640

# 4

def f4(x):
    return x**7 + 0.5*x - 0.5

def corda(a,b):
    for i in range(5):
        w = (a*f4(b) - b*f4(a)) / (f4(b)- f4(a))
        print(i, a , b, w)
        if (f4(a)*f4(w) < 0):
            b = w
        else:
            a = w
            
# corda(0,0.8)

# 0.656044  0.8     0.731147
# 0.731147  0.8     0.742964
# 0.742964  0.8     0.744755

# Aplica-se (Fundamental)
# Não se aplica
# Aplica-se (Fundamental)
# Aplica-se


# 5

def f(t,y,z):
    return z

def df(t,y,z):
    return 0.5 + t**2 + t*z

def euler(t,y,z,h):
    print(0,t,y)
    for i in range(5):
        y0 = y
        z0 = z
        y += h* f(t,y0,z0)
        z += h* df(t,y0,z0)
        t += h
        print(i+1,t,y)
        
# euler(0,0,1,0.25)

def rk4(t,y,z,h):
    print(0,t,y)
    for i in range(5):
        d1 = h* f(t, y, z)
        l1 = h* df(t, y, z)
        d2 = h* f(t + h/2, y + d1/2, z + l1/2)
        l2 = h* df(t + h/2, y + d1/2, z + l1/2)
        d3 = h* f(t + h/2, y + d2/2, z + l2/2)
        l3 = h* df(t + h/2, y + d2/2, z + l2/2)
        d4 = h* f(t + h, y + d3, z + l3)
        l4 = h* df(t + h, y + d3, z + l3)
        
        y += d1/6 + d2/3 + d3/3 + d4/6
        z += l1/6 + l2/3 + l3/3 + l4/6
        t += h
        
        print(i+1,t,y)
        
# rk4(0, 0, 1, 0.25)
        
        
# 0.000000    0.000000
# 0.250000    0.250000
# 0.500000    0.531250

# 0.000000    0.000000
# 0.250000    0.268742
# 0.500000    0.592204


# 6

a = 0
b = 2
h = 0.5

def f6(x):
    return math.sqrt(1 + (1.5*math.exp(1.5*x))**2)

def simpson(a,b,h):
    n = int((b-a)/h)
    sum = 0
    for i in range(n+1):
        if (i == 0 or i == n):
            sum += f6(a + i*h)
        elif (i % 2 == 0):
            sum += 2*f6(a + i*h)
        elif (i % 2 == 1):
            sum += 4* f6(a + i*h)
    return h/3 * sum

def trapezio(a,b,h):
    n = int((b-a)/h)
    sum = 0
    for i in range(n+1):
        if (i == 0 or i == n):
            sum += f6(a + i*h)
        else:
            sum += 2 * f6(a + i*h)
        
    return h/2 * sum

def errt(a,b,h):
    return (trapezio(a, b, h/4) - trapezio(a, b, h/2)) / 3

def errs(a,b,h):
    return (simpson(a, b, h/4) - simpson(a, b, h/2)) / 15   

def qct(a,b,h):
    return (trapezio(a, b, h/2) - trapezio(a, b, h)) / (trapezio(a, b, h/4) - trapezio(a, b, h/2)) 

def qcs(a,b,h):
    return (simpson(a, b, h/2) - simpson(a, b, h)) / (simpson(a, b, h/4) - simpson(a, b, h/2)) 
    
    
print(trapezio(a, b, h),simpson(a, b, h))
print(trapezio(a, b, h/2), simpson(a, b, h/2))
print(trapezio(a, b, h/4), simpson(a, b, h/4))
print()
print(qct(a, b, h),qcs(a, b, h))
print()
print(errt(a, b, h),errs(a, b, h))

# 0.25      0.25
# 0.125     0.125

# 20.183134 19.320732
# 19.514364 19.291441
# 19.345729 19.289517

# 3.965775 15.225153

# -0.056212 -0.000128



        
            
            


















    