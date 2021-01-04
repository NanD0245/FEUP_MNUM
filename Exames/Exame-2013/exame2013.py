import math
# 1.

A = 0.5
h = 0.25
t0 = 0
y0 = 0
dy0 = 0

def dydt(t,y,z):
    return z

def dzdt(t,y,z):
    return A + t**2 + t*z

def euler(t,y,z,h):
    print(str(0) + " t: " + str(t) + " y: " + str(y) + " z: " + str(z))
    for i in range(1,3):
        y0 = y
        z0 = z
        y += dydt(t,y0,z0)*h
        z += dzdt(t,y0,z0)*h
        print(str(i) + " t: " + str(t) + " y: " + str(y) + " z: " + str(z))
        t += h
        
# euler(t0,dy0,y0,h)
# print("\n\n")

# n = 0     t = 0.00      y = 0
# n = 1     t = 0.25      y = 0
# n = 2     t = 0.50      y = 0.03125


def rk4(t,y,z,h):
    print(str(0) + " t: " + str(t) + " y: " + str(y) + " z: " + str(z))
    for i in range(1,3):
        d1 = h*dydt(t,y,z) 
        l1 = h*dzdt(t,y,z)  
        d2 = h*dydt(t + h/2, y + d1/2, z + l1/2)
        l2 = h*dzdt(t + h/2, y + d1/2, z + l1/2)
        d3 = h*dydt(t + h/2, y + d2/2, z + l2/2)
        l3 = h*dzdt(t + h/2, y + d2/2, z + l2/2)
        d4 = h*dydt(t + h, y + d3, z + l3)
        l4 = h*dzdt(t + h, y + d3, z + l3)

        y += d1/6 + d2/3 + d3/3 + d4 / 6
        z += l1/6 + l2/3 + l3/3 + l4 / 6
        t += h
        print(str(i) + " t: " + str(t) + " y: " + str(y) + " z: " + str(z))
        
        
# rk4(t0,y0,dy0,h)

# n = 0     t = 0.00      y = 0
# n = 1     t = 0.25      y = 0.01612
# n = 2     t = 0.50      y = 0.07058

# 2.

# Como podemos ver através do maxima, a solução será arredondadamente x = 5.538, 
# y = 69.2307 e z = 12.30769, assim podemos concluir que a soluçao obtida pelo
# método com pivotagem será a mais correta pois tem um erro menor que a soluçao 
# obtida pelo metodo com pivotagem.

# Não se obtiveram resultados iguais devido às aproximações realizadas nos
# cálculos pela máquina. No caso sem pivotagem, o facto de estarmos a usar
# 1e-5 como valor pivot para a primeira coluna, são introduzidos erros pelo
# facto de se estar a operar com um número pequeno em V.F.

# Qualquer tipo de erros nos dados, quer de coeficientes das incognitas quer de termos
# independentes irá aumentar o erro na soluçao final, afastando ainda mais a soluçao obtida com 
# a soluçao real.


# 3

def f3(x,y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x

def df3dx(x,y):
    return -y + 6*x -8

def df3dy(x,y):
    return 2*y-x+11

def gradiente(x, y, h, n):
    print("{0}: {1:.2f} | {2:.7f} | {3:.7f} | {4:.7f} | {5:.7f}".format(0, x, y, f3(x, y), df3dx(x, y), df3dy(x, y)))
    for i in range(n):
        xo = x
        yo = y
        x -= h * df3dx(xo, yo)
        y -= h * df3dy(xo, yo)
        if f3(x, y) < f3(xo, yo):
            h *= 2
        else:
            x = xo
            y = yo
            h /= 2
        print("{0}: {1:.2f} | {2:.7f} | {3:.7f} | {4:.7f} | {5:.7f}".format(i+1, x, y, f3(x, y), df3dx(x, y), df3dy(x, y)))

# gradiente(2, 2, 0.5,3)

# n = 0   x = 2           Z(x) = 18           g = 2       h = 0.5
#         y = 2                               g = 13
        
# n = 1   x = 1           Z(x) = -29.75       g = 2.5
#         y = -4.5                            g = 1

# 4

c = 1.5
a = 1.0
b = 1.5
h = 0.125

def f4(x):
    return math.e**(c*x)

def simpson(a,b,h):
    n = int((b-a)/h)
    sum = 0
    for i in range(n+1):
        if (i == 0 or i == n):
            sum += f4(a+i*h)
        elif (i % 2 == 0):
            sum += 2* f4(a+i*h)
        elif (i % 2 == 1):
            sum += 4*f4(a+i*h)
        
    return (h/3)*sum

# print(simpson(a, b, h))
# print(simpson(a,b,h/2))
# print(simpson(a,b,h/4))
err = (simpson(a,b,h/4) - simpson(a,b,h/2)) / 15
# print("err: " + str(err))
qc = (simpson(a, b, h/2)- simpson(a, b, h)) / (simpson(a, b, h/4)-simpson(a, b, h/2))
# print("qc: " + str(qc))

# a)

# h = 0.125     S = 3.33739
# h = 0.0625    S = 3.33737
# h = 0.03125   S = 3.33736

# err = 0.00000
# qc = 15.94745

# b)
# 3.33736

# c)
# 0.00000

# 5

def f5(x):
    return x - 3.7 + math.cos(x+1.2)**3
    
def df5(x):
    return 1- 3 * math.cos(x+1.2)**(2) * math.sin(x+1.2)

def newton(x):
    x = x - f5(x)/df5(x)
    print(x)

# newton(3.8)
# 3.70026
    
    

