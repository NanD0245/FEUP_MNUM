def f(x,y):
    return x-2

def fy(x,y,z):
    return z

def fz(x,y,z):
    return x -3*z -2*y
        
def rk2_3var(x, y, z, h, n, f, g):
    print(0, ":", x, y)
    for i in range(1,n+1):
        y1 = y + h*f(x+h/2,y+(h/2)*f(x,y,z),z+(h/2)*g(x,y,z))
        z1 = z + h*g(x+h/2,y+(h/2)*f(x,y,z),z+(h/2)*g(x,y,z))
        x1 = x + h
        x = x1
        y = y1
        z = z1
        print(i, ":",x,y,z)
        
# rk2(0,3,0.5,50,f)

rk2_3var(0,0,0,0.5,50,fy,fz)