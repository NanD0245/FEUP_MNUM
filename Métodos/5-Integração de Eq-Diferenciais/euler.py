def f(x,y):
    return x-2

def fy(x,y,z):
    return z

def fz(x,y,z):
    return x -3*z -2*y

def euler(x, y, h, n, f):
    print(0, ":", x, y)
    for i in range(1,n+1):
        y += h * f(x, y)
        x += h
        print (i, ":", x, y)
        
def euler_3var(x, y, z, h, n, f, g):
    print (0, ":", x, y, z)
    for i in range(1,n+1):
        yn = y
        zn = z
        y += h * f(x, yn, zn)
        z += h * g(x, yn, zn)
        x += h
        print (i, ":", x, y, z)
        
# print(euler(0,3,0.5,50,f))

print(euler_3var(0,0,0,0.5,50,fy,fz))