import math
# 1

def f1(x):
    return math.sin(x) + x**5 - 0.2*x + 1

def bissecao(a,b):
    print(0,a,b)
    for i in range(6):
        m = (a+b)/2
        if (f1(a)*f1(m) < 0):
            b = m
        else:
            a = m
        print(i+1,a,b)
    print(b-a)
        
bissecao(-1,0)
        
        


# a) 1

# b) ]-1,0[

# c) -0.828125
#    0.015625
#    1.88679



# 2

def f(x,y):
    return x**2 - y - 1.2

def dfx(x,y):
    return 2*x

def dfy(x,y):
    return -1

def g(x,y):
    return -x + y**2 - 1.0

def dgx(x,y):
    return -1

def dgy(x,y):
    return 2*y

def newton(x,y):
    print(0,x,y)
    for i in range(2):
        x0 = x - (f(x, y)*dgy(x, y) - g(x, y)*dfy(x, y)) / (dfx(x, y)*dgy(x, y) - dgx(x, y)*dfy(x, y))
        y0 = y - (g(x, y)*dfx(x, y) - f(x, y)*dgx(x, y)) / (dfx(x, y)*dgy(x, y) - dgx(x, y)*dfy(x, y))
        x = x0
        y = y0
        print(i+1,x,y)
        
# newton(1,1)

# 1 2.133333 2.066667
# 2 1.745801 1.697640



# 3

a = 0
b = 2
h = 0.25

def l(x):
    return math.sqrt(1+(1.5*math.exp(1.5*x))**2)

def trapezio(a,b,h):
    n = int((b-a)/h)
    sum = 0
    for i in range(n+1):
        if (i == 0 or i == n):
            sum += l(a + i*h)
        else:
            sum += 2*l(a+ i*h)
    return h/2*sum


def simpson(a,b,h):
    n = int((b-a)/h)
    sum = 0
    for i in range(n+1):
        if (i == 0 or i == n):
            sum += l(a + i*h)
        elif (i % 2 == 0):
            sum += 2*l(a+i*h)
        elif (i%2 == 1):
            sum += 4*l(a+i*h)
            
    return h/3 * sum

lt1 = trapezio(a, b, h)
lt2 = trapezio(a, b, h/2)
lt3 = trapezio(a, b, h/4)

ls1 = simpson(a, b, h)
ls2 = simpson(a, b, h/2)
ls3 = simpson(a, b, h/4)

qct = (lt2 - lt1) / (lt3 - lt2)
qcs = (ls2 - ls1) / (ls3 - ls2)

errt = (lt2 - lt1) / 3
errs = (ls2 - ls1) / 15

# print(h , h/2 , h/4)
# print(lt1,ls1)
# print(lt2,ls2)
# print(lt3,ls3)
# print()
# print(qct,qcs)
# print()
# print(errt,errs)

# 0.25 
# 0.125 
# 0.0625

# 19.514364 19.291440
# 19.345729 19.289517
# 19.303479 19.289395

# 3.991351 15.793330

# -0.056212 -0.000128



# 4

def f4(t,T):
    return T

def dz(t,T):
    return -0.25*(T-59)

def euler(t,T,h):
    for i in range(2):
        T += h*dz(t,T)
        t += h
    return T

# print(euler(2,2,0.5))

# 15.359375



# 5

def F(x):
    return -5*math.cos(x) + math.sin(x) + 10

def aurea(x1,x2):
    B = (math.sqrt(5) - 1) / 2
    A = B**2
    for i in range(2):
        x3 = A*(x2-x1) + x1
        x4 = B*(x2-x1) + x1
        print(x1,x2,x3,x4,F(x1),F(x2),F(x3),F(x4))
        if (F(x3) < F(x4)):
            x1 = x3
        elif (F(x3) > F(x4)):
            x2 = x4
            
# aurea(0,6)

# 0 6        2.291796 3.708204 5.0 4.919733  14.051826 13.681848
# 0 3.708204 1.416408 2.291796 5.0 13.681848 10.219226 14.051826


# 6

def A(x,y):
    return 3*x**2 - x*y + 11 *y + y**2 - 8*x

def Ax(x,y):
    return 6*x - y - 8

def Ay(x,y):
    return -x + 11 + 2*y

def gradiente(x,y,h):
    # print(x,y,A(x,y))
    for i in range(1):
        x0 = x
        y0 = y
        x -=  h*Ax(x0,y0)
        y -= h*Ay(x0,y0)
        if (A(x,y) > A(x0,y0)):
            h = h/2
            x = x0
            y = y0
        elif (A(x,y) < A(x0,y0)):
            h = h*2
        # print(x,y,A(x,y),Ax(x,y),Ay(x,y))
        
# gradiente(2,2,0.5)

# n = 0   x = 2           Z(x) = 18           g = 2       h = 0.5
#         y = 2                               g = 13
        
# n = 1   x = 1           Z(x) = -29.75       g = 2.5
#         y = -4.5                            g = 1

    
        

        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
