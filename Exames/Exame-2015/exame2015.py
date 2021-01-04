import math
# 1

Ta = 37

def z(t,x):
    return -0.25 * (x-Ta)

def euler(t,x,h):
    print(0,t,x)
    for i in range(3):
        x += h * z(t,x)
        t += h
        print(i+1,t,x)
        
# euler(5,3,0.4)
        
# 9.46


# 2

# 1. A soma acumulada de números inteiros tem pouca suscetibilidade a erros de
# arredeondamento, o que aumenta a fiabilidade dos resultados, contudo,
# como só é possível iterar em intervalos inteiros, a definição dos resultados
# está limitada.
# 2. A soma acumulada de números em vírgula flutuante tem muita propensão a
# erros de arredondamento, devido aos sucessivos arredondamentos da mantissa.
# Tem a vantagem de permitir obter resultados mais granulares do que o iterador
# 1, mas a desvantagem de uma considerável perda de precisão à medida que o
# número de iterações aumenta.
# 3. Neste iterador são somados, à semelhança do iterados 2, números em vírgula
# flutuante, no entanto, esta não é uma soma acumulada. O valor a somar ao valor
# inicial é atualizado por meio de uma multiplicação com um inteiro, o que
# diminui o erro cometido pela acumulação de somas. Assim, este iterador
# apresenta a vantagem de permitir maior granularidade que 1 e maior precisão que
# 2, mas a desvantagem de continuar suscetível a alguns erros na soma de VF.
# Por exemplo, no caso em que as ordens de grandeza de x0 e h são muito díspares,
# o resultado da adição poderia simplesmente ser igual ao maior dos dois números.
# 4. Este iterador é tão suscetível a erros como o 2. É efetuada uma soma
# acumulada de números em vírgula flutuante. Como a fração exponenciada tem
# representação absoluta em binário, desta operação não são criados mais erros do
# que se a soma fosse acumulando um valor constante. No entanto, como este valor
# é decrescente, quando atingir uma ordem de grandeza muito menor do que xn, a
# precisão do resultado da adição será prejudicada, sendo que no pior caso o
# valor do iterador deixa de variar. Tem como vantagem permitir variar o valor do
# iterador de uma maneira que pode ser útil, mas a desvantagem de se
# realizarem muitas operações com vírgula flutuante e de as ordens de grandeza
# dos números se afastarem progressivamente.

# 3

A = [[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]]
b = [-1, 1, 1]

def gauss(A, b):
    for col in range(len(A) - 1):
        for line in range(col + 1, len(A)):
            m = A[line][col] / A[col][col]
            A[line] = [A[line][i] - m * A[col][i] for i in range(len(A))]
            b[line] -= m * b[col]
        m = 1 / A[col+1][col+1]
        A[col+1] = [A[col+1][i] * m for i in range(len(A))]
        b[col+1] *= m
    print("Triangular inferior:")
    print(A)
    print(b)
    print()
    for col in range(len(A) - 1):
        for line in range(col + 1, len(A)):
            m = A[len(A) - 1 - line][len(A) - 1 - col] / A[len(A) - 1 - col][len(A) - 1 - col]
            A[len(A) - 1 - line] = [A[len(A) - 1 - line][i] - m * A[len(A) - 1 - col][i] for i in range(len(A))]
            b[len(A) - 1 - line] -= m * b[len(A) - 1 - col]
    print("Solução:")
    print(A)
    print(b)
    print()
    return b.copy()

def est_ext(err):
    x = gauss(A.copy(), b.copy())
    dAx = [sum(err * x[j] for j in range(len(A))) for i in range(len(A))]
    dbdAdx = [err - dAx[i] for i in range(len(A))]
    gauss(A.copy(), dbdAdx.copy())

# gauss(A, b)

est_ext(0.05)

# 0.5    0.333333    -1
#        1.000000    18.000000
#                    -30.000000

# x1 = -15.000000
# x2 = 48.000000
# x3 = -30.000000

# 0.5,   0.333333     -0.300000
#        1.000000     2.400000
#                     -3.000000

# x3

 

# 4

def f4(x):
    return math.e**x -4*x**2

def g1(x):
    return 2*math.log(2*x)

def picard(x):
    for i in range(3):
        x0 = g1(x)
        print(x0)
        print(x0-x)
        x = x0
        
# picard(1.1)


# converge se: |g'(x)| < 1
# a) X1 e X2
# b) nenhuma
# c) X1 e X2

# d) 1.1
#    1.5769147

# e) 0.4769147

# 5

a = 0
b = 1
h = 0.125


def f(x):
    return math.e**(2.5*x)

def df(x):
    return  math.sqrt(1 + (2.5 * math.exp(2.5 * x)) ** 2)

def simpson(a,b,h):
    n = int((b-a)/h)
    sum = 0
    for i in range(n+1):
        if (i == 0 or i == n):
            sum += df(a+i*h)
        elif (i%2 == 0):
            sum += 2*df(a+i*h)
        elif (i%2 == 1):
            sum += 4*df(a+i*h)
    
    return h/3 * sum

def trapezios(a,b,h):
    n = int((b-a)/h)
    sum = 0
    for i in range(n+1):
        if (i == 0 or i == n):
            sum += df(a+i*h)
        else:
            sum += 2*df(a+i*h)
    
    return h/2 * sum

# print(trapezios(a, b, h), "        " , simpson(a, b, h))
# print(trapezios(a, b, h/2), "        " , simpson(a, b, h/2))
# print(trapezios(a, b, h/4), "        " , simpson(a, b, h/4))

# qc:
# print((trapezios(a, b, h/2) - trapezios(a, b, h)) / (trapezios(a, b, h/4) - trapezios(a, b, h/2)))
# print((simpson(a, b, h/2) - simpson(a, b, h)) / (simpson(a, b, h/4) - simpson(a, b, h/2)))

# err:
# print(abs(trapezios(a, b, h/4)-trapezios(a, b, h/2)) / 3)
# print(abs(simpson(a, b, h/4)-simpson(a, b, h/2)) / 15)

# a javardo xD
# print(abs(trapezios(a, b, h/4) - 11.25490891706089))
# print(abs(simpson(a, b, h/4) - 11.25490891706089))

# 0.06250            0.06250

# 11.346293          11.255495
# 11.277783          11.254946
# 11.260629          11.254911

#  3.993940          15.857980

#  0.005720          0.0000023



# 6


# O método númerico mais adequado é o de Levenberg-Marquardt.
# Este método é uma combinação do método do gradiente com o método da quádrica.
# Assim, colmata os problemas de um dos métodos com as vantagens do outro,
# aliando o melhor desempenho do método da quádrica na vizinhança, extendendo a
# sua aplicabilidade para lá da vizinhança deste. Também é um método que lida
# bem com depressões alongadas, já que a quádrica permite detetar esse
# alongamento. Esse caso verifica-se nesta função.
# ???Outra situação complicada que surge no caso apresentado é o da proximidade
# entre mínimos. O método irá convergir para um deles, no entanto este pode não
# ser o menor ou ter características que não se aplicam ao contexto mais alargado
# do problema. Para combater isso seria necessário definir constrições a aplicar
# ao método de modo a "forçar" a convergência para o mínimo pretendido.???


# 7

a = 1.5
b = 4.2


def f7(x):
    return x**3 -10*math.sin(x) +2.8 

def bissecao(a,b):
    print(0,b)
    for i in range(3):
        m = (a+b) / 2
        if (f7(a) * f7(m) < 0):
            b = m
        else:
            a = m
        print(i+1,b)

# bissecao(a, b)

# 2.1750















