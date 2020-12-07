def f(x):
    return x**4 + 2*x**3 - x - 1

a0 = 0
b0 = 1

def bisseccao(f,a0,b0):
    an = a0
    bn = b0
    for i in range(50):
        m = (an+bn)/2
        if (f(an)*f(m) < 0):
            bn = m
        else:
            an = m
    return (an,bn,m)

print(bisseccao(f, a0, b0))