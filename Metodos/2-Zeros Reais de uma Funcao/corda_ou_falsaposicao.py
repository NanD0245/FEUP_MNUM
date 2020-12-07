def f(x):
    return x**4 + 2*x**3 - x - 1

a0 = 0
b0 = 1

def corda(f,a0,b0):
    an = a0
    bn = b0
    for i in range(50):
        w = (an*f(bn)-bn*f(an))/(f(bn)-f(an))
        if (f(an)*f(w)<0):
            bn = w
        else:
            an = w
    return (an,bn,w)

print(corda(f, a0, b0))
                