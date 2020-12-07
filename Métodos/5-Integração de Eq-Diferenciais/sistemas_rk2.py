def g(x,y,z):
    return x+y+z

def f(x,y,z):
    return 2*x-y-z

def rk2_3var(x, y, z, xf, n, f, g):
    print(0, ":", x, y)
    h = (xf-x)/n
    for i in range(1,n+1):
        y1 = y + h*f(x+h/2,y+(h/2)*f(x,y,z),z+(h/2)*g(x,y,z))
        z1 = z + h*g(x+h/2,y+(h/2)*f(x,y,z),z+(h/2)*g(x,y,z))
        x1 = x + h
        x = x1
        y = y1
        z = z1
        print(i, ":",x,y,z)
        
rk2_3var(0,1,1,5,10,f,g)
        
