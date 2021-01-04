import math

# 1

def f1(x,y):
    return math.sin(x+y) - math.exp(x-y)

def dfx(x,y):
    return math.cos(x+y) - math.exp(x-y)

def dfy(x,y):
    return math.cos(x+y) + math.exp(x-y)

def g1(x,y):
    return math.cos(x+y) - x**2 * y**2

def dgx(x,y):
    return -math.sin(y+x) -2*x*y**2

def dgy(x,y):
    return -math.sin(y+x) -2*y*x**2

def newton(x,y):
    print(0,x,y)
    for i in range(2):
        x0 = x
        y0 = y
        x = x0 - (f1(x0,y0) * dgy(x0,y0) - g1(x0,y0) * dfy(x0,y0)) / (dfx(x0,y0) * dgy(x0,y0) - dgx(x0,y0) * dfy(x0,y0))
        y = y0 - (g1(x0,y0) * dfx(x0,y0) - f1(x0,y0) * dgx(x0,y0)) / (dfx(x0,y0) * dgy(x0,y0) - dgx(x0,y0) * dfy(x0,y0))
        print(i+1,x,y)
        
newton(0.5,0.25)
        
#1 0.500000    0.992145    0.723879
#2 0.250000    0.683701    0.662607



# 2

# a) I

# b) III

# c)

# (1.2  +  -61y  +  -41z)/  103
# (0  +  -1x  +  -3z)/  5.5
# (-13  +  -2x  +  -10y)/  -13



# 3

def f3(x,y):
    if (x == 0):
        if (y == 0): return 1.1
        if (y == 1): return 2.1
        if (y == 2): return 7.8
    elif (x == 1):
        if (y == 0): return 1.4
        if (y == 1): return 4.0
        if (y == 2): return 1.5
    elif (x == 2):
        if (y == 0): return 9.8
        if (y == 1): return 2.2
        if (y == 2): return 1.2
        

s = (f3(0,0) + f3(2,2) + f3(0,2) + f3(2,0) + 4*(f3(1,0) + f3(0,1) + f3(2,1) + f3(1,2)) + 16 * f3(1,1)) * 1 * 1 / 9

# print(s)
    
# 12.522222



# 4

def z(x,y,t):
    return t

def dz(x,y,t):
    return - 7 * t - 4 * y  

def euler(x,y,t,h):
    print(0,x,y,t)
    for i in range(4):
        y0 = y
        t0 = t
        y += h * z(x,y0,t0)
        t += h * dz(x,y0,t0)
        x += h
        print(i+1,x,y,t)
        
# euler(0.4,2,1,0.2)
    

# z

# -By + Az

# 0.4 2 1
# 0.6 2.2    -2.0
# 0.8 1.8    -0.96
# 1.0 1.608  -1.056



# 5



# 6

a = 0.4523*10**4
b = 0.2115*10**(-3)
c = 0.2583*10**1
s = a+b+c
# print(s)
# print(4525 - s)
# print((4525 - s) / s)

# 0.4525 E4
# 0.5832 E0
# 0.0129 %
 


















































