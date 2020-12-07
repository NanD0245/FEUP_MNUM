# aula ----------------------

def df(x,y):
    return x**2

def sp(x,y):
    return x**3/3+1

def rk4_aula(x,y,xf,n,f):
    h = (xf-x)/n
    for i in range(1, n+1):
        d1 = h * f(x, y)
        d2 = h * f(x + h/2, y + d1/2)
        d3 = h * f(x + h/2, y + d2/2)
        d4 = h * f(x + h, y + d3)
        
        y += d1/6.0 + d2/3.0 + d3/3.0 + d4/6.0
        x += h
        print(i, ":", x, y, "error =", sp(x,y)-y)

rk4_aula(0, 1, 5, 10, df)


print(sp(5,1))

# ------------------------------------

# def f(x,y):
#     return x-2

# def fy(x,y,z):
#     return z

# def fz(x,y,z):
#     return x -3*z -2*y

# def rk4(x, y, h, n, f):
#     print(0, ":", x, y)
#     for i in range(1, n+1):
#         d1 = h * f(x, y)
#         d2 = h * f(x + h/2, y + d1/2)
#         d3 = h * f(x + h/2, y + d2/2)
#         d4 = h * f(x + h, y + d3)
        
#         y += d1/6 + d2/3 + d3/3 + d4/6
#         x += h
#         print(i, ":", x, y)
        
# def rk4_3var(x, y , z, h, n, f, g):
#     print(0, ":", x, y, z)
#     for i in range(1, n+1):
#         d1 = h * f(x, y, z)
#         l1 = h * g(x, y, z)
#         d2 = h * f(x + h/2, y + d1/2, z + l1/2)
#         l2 = h * g(x + h/2, y + d1/2, z + l1/2)
#         d3 = h * f(x + h/2, y + d2/2, z + l2/2)
#         l3 = h * g(x + h/2, y + d2/2, z + l2/2)
#         d4 = h * f(x + h, y + d3, z + l3)
#         l4 = h * g(x + h, y + d3, z + l3)
        
#         z += l1/6 + l2/3 + l3/3 + l4/6
#         y += d1/6 + d2/3 + d3/3 + d4/6
#         x += h
#         print(i, ":", x, y, z)
        
# # rk4(0,3,0.5,50,f)

# rk4_3var(0, 0, 0, 0.5, 50, fy, fz)