import math
# 2

a = 0
b = 1
h = 0.125

def l(x):
    return math.sqrt(1 + (2.5*math.exp(2.5*x))**2)

def trapezios(a,b,h):
    n = int((b-a)/h)
    sum = 0
    for i in range(n+1):
        if (i == 0 or i == n):
            sum += l(a+i*h)
        else:
            sum += 2*l(a+i*h)
    return h/2 * sum


def simpson(a,b,h):
    n = int((b-a)/h)
    sum = 0
    for i in range(n+1):
        if (i == 0 or i == n):
            sum += l(a+i*h)
        elif (i%2 == 0):
            sum += 2* l(a+i*h)
        elif (i%2 == 1):
            sum += 4* l(a+i*h)
    return h/3*sum


At = trapezios(a, b, h)
As = simpson(a, b, h)
bt = trapezios(a, b, h/2)
bs = simpson(a, b, h/2)
ct = trapezios(a, b, h/4)
cs = simpson(a, b, h/4)

errt = (ct - bt) / 3
errs = (cs - bs) / 15 

qct = (bt - At) / (ct - bt)
qcs = (bs - As) / (cs - bs)

# print(h/2, h/2)
# print(h/4,h/4)
# print()
# print(At, As)
# print(bt,bs)
# print(ct,cs)
# print()
# print(qct,qcs)
# print()
# print(errt,errs)


# 4

def dc(t,C,T):
    return -math.exp(-0.5 / (T + 273))*C

def dt(t,C,T):
    return 30*math.exp(-0.5 / (T + 273))*C - 0.5*(T-20)

def euler(t,C,T,h,n):
    # print(0,t,C,T)
    for i in range(n):
        C0 = C
        T0 = T
        C += h * dc(t,C0,T0)
        T += h * dt(t,C0,T0)
        t += h
        # print(i+1,t,C,T)
    return T
        
# euler(0,2.5,25,0.25)
     
# 0 2.5 25
# 0.25 1.876048 43.093567
# 0.50 1.407777 54.254990

def rk4(t,C,T,h):
    print(0,t,C,T)
    for i in range(2):
        d1 = h * dc(t,C,T)
        l1 = h * dt(t, C, T)
        d2 = h * dc(t + h/2, C + d1/2, T + l1/2)
        l2 = h * dt(t + h/2, C + d1/2, T + l1/2)
        d3 = h * dc(t + h/2, C + d2/2, T + l2/2)
        l3 = h * dt(t + h/2, C + d2/2, T + l2/2)
        d4 = h * dc(t + h, C + d3, T + l3)
        l4 = h * dt(t + h, C + d3, T + l3)
        
        C += d1/6 + d2/3 + d3/3 + d4/6
        T += l1/6 + l2/3 + l3/3 + l4/6
        t += h
        print(i+1,t,C,T)
        
# rk4(0,2.5,25,0.25)

# 0 2.5 25
# 0.25 1.947816 39.943493
# 0.50 1.517572 49.701360

ae = euler(0,2.5,25,0.25,2)
be = euler(0,2.5,25,0.125,4)
print(be)
ce = euler(0,2.5,25,0.0625,8)
print(ce)

er = ce - be
qc = (be - ae) / (ce - be)

print(er,qc) 

# 0.1250 51.770668
# 0.0625 50.692055
# 2.303255
# -1.078614 


# 5

def w(x,y):
    return -1.1*x*y + 12*y + 7 * x**2 - 8 * x

def dwdx(x,y):
    return -1.1*y + 14*x - 8

def dwdy(x,y):
    return -1.1*x + 12

def gradiente(x,y,h):
    for i in range(1):
        x0 = x
        y0 = y
        x -= h * dwdx(x0,y0)
        y -= h * dwdy(x0,y0)
        if (w(x,y) < w(x0,y0)):
            h = 2*h
        else:
            y = y0
            x = x0
            h = h/2
    return w(x,y)

# print(gradiente(3,1,0.1))
    
# 4.510170























