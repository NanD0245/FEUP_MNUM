import math
# 1

def f1(x):
    return x**4 - 4*x**3 + x - 1

def picard_peano(x,g):
    count = 0
    while (abs(f1(x)) > 1e-5 and count < 5):
        x = g(x)
        count += 1
        print(x)
        
def g1(x):
    return (4*x**2 - 1/x**2 - 1/x**3)

def g2(x):
    return (4 - 1/x**2 - 1/x**3)

def g3(x):
    return (-x**4 + 4*x**3 + 1)

def g4(x):
    return (4*x**3-x+1)**(1/4)
    
# picard_peano(4, g4)

# a) 2

# b) menor positiva = 3.95

# [0, +inf] -> sim
# [-0.2, 4] -> sim
# [1 , 3.5] -> não
# [3.5,4.5] -> sim

# c)

#    ca -> sim
#    cb -> sim
#    cc -> não

# d)
    # n = 0   x = 4
    # n = 1   x = 3.988229
    # n = 2   x = 3.979366


# 2

A = [[0.1, 0.5, 3, 0.25],
     [1.2, 0.2, 0.25, 0.2],
     [-1, 0.25, 0.3, 2],
     [2, 1e-5, 1, 0.4]]

b = [0, 1, 2, 3]


def gauss(A, b):
    dim = len(A)
    for col in range(dim - 1):
        if (abs(A[col][col] - 1) > 1e-6):
            m = 1 / A[col][col]
            A[col] = [A[col][i] * m for i in range(dim)]
            b[col] *= m
        for line in range(col + 1, dim):
            m = A[line][col] / A[col][col]
            A[line] = [A[line][i] - m*A[col][i] for i in range(dim)]
            b[line] -= m*b[col]
    if (abs(A[dim-1][dim-1] - 1) > 1e-6):
            m = 1 / A[dim-1][dim-1]
            A[dim-1] = [A[dim-1][i] * m for i in range(dim)]
            b[dim-1] *= m
    print("Triangular inferior:")
    print(A)
    print(b)
    print()
    for col in range(dim - 1):
        for line in range(col + 1, dim):
            m = A[dim - 1 - line][dim - 1 - col] / A[dim - 1 - col][dim - 1 - col]
            A[dim - 1 - line] = [A[dim - 1 - line][i] - m*A[dim - 1 - col][i] for i in range(dim)]
            b[dim - 1 - line] -= m*b[dim - 1 - col]
    print("Solução:")
    print(A)
    print(b)
    print()
    return b

def est_ext(A, b, err):
    dim = len(A)
    x = gauss(A.copy(), b.copy())
    dAx = [sum(err * x[i] for i in range(dim)) for j in range(dim)]
    dbdAx = [err - dAx[i] for i in range(dim)]
    return gauss(A.copy(), dbdAx.copy())

# gauss(A,b)

# print(est_ext(A, b, 0.3))

# a)

# 6.163793    0.482759     -0.172414
#            -0.954175     -1.410337
#                           1.820376

# b)

# x1 = 0.972630
# x2 = -3.064432
# x3 = 0.326620
# x4 = 1.820376

# c)

# x1 = 0.122491
# x2 = 0.567001
# x3 = -0.015301
# x4 = 0.134387


# 3

def dxdt(t,x,z):
    return z

def dzdt(t,x,z):
    return (-z-5*x)/20

def euler(t,x,z,h):
    for i in range(30):
        x0 = x
        z0 = z
        z += h* dzdt(t,x0,z0)
        x += h* dxdt(t,x0,z0)
        t += h 
        print(t,x)
        
        
# newton(0, 1, 0, 0.2)

# a) 0.2

# b) 1

# c) 5

# 4

# 5

# - Entre os métodos discutidos na UC, o de Simpson é o que apresenta maior
#     precisão, pois substitui a curva por uma parábola e não por uma corda no
#     intervalo considerado. Assim, garante-se, geralmente, um ajuste mais
#     correto à função.
#     - O método dos trapézios é um método de segunda ordem pois o erro varia com
#     o quadrado do passo de integração.
#     - O método de Simpson é um método de quarta ordem pois o erro varia com a
#     quarta potência do passo de integração.
#     - Para além do passo o erro também é influenciado pela própria integranda,
#     o parametro ξ incontrolável.
#     - Para estimar o erro, deve-se calcular o integral com o método escolhido
#     variando o h.
#     - Para garantir a validade do erro calculado, é necessário garantir que o
#     valor de h é suficientemente pequeno. Essa garantia é obtida calculando o
#     quoeficiente de convergência.
#     - Depois de establecer qual o h para o qual o QC se adequa à ordem do
#     método, deve-se ajustar h ao erro máximo pretendido.


# 6

def f6(x):
    return x + (x-2)**2 / (math.sin(x)+4)

def aurea_min(x1,x2):
    B = (math.sqrt(5) - 1) / 2
    A = B**2
    while (abs(x2-x1) > 1e-7):
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        fx1 = f6(x1)
        fx2 = f6(x2)
        fx3 = f6(x3)
        fx4 = f6(x4)
        print("""{0}: {1:.7f} | {2:.7f} | {3:.7f} | {4:.7f} | {5:.7f} | {6:.7f} | {7:.7f} | {8:.7f}""".format(0, x1, x2, x3, x4, fx1, fx2, fx3, fx4))
        if fx3 < fx4:
            x2 = x4
        else:
            x1 = x3
        print("Intervalo: {0:.7f} - {1:.7f}".format(x1, x2))
        print("Amplitude: {0:.7f}".format(abs(x1-x2)))

# aurea_min(-1, 1.5)

# -1          0.545085    -0.409830   -0.045085    1.849428    1.013555    1.202611    1.012424
# -0.409830   0.545085    -0.045085   0.180340     1.202611    1.013555    1.012424    0.972605

# 0.59017


# 7

def f(x):
    return -x + 60*math.cos(math.sqrt(x)) +2

def df(x):
    return -30*math.sin(math.sqrt(x))/math.sqrt(x)-1

def newton(x):
    print(x,f(x))
    for i in range(3):
        x = x - f(x)/df(x)
        print(x,f(x))
        
newton(1.8)

# a) 3
# b) 1.8           13.829313
   # 2.407184       0.749905
   # 2.444067
 
# c) 1 







