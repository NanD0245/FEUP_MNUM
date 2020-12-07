def f(x):
    return x**4 + 2*x**3 - x - 1

def df(x):
    return 4*x**3 + 6*x**2 - 1

def newton(x):
    return x - f(x) / df(x)

guess = float(input("GUESS: "))

for i in range(0,20,1):
    guess = newton(guess)
    print(guess)
    
print("ROOT: {0}".format(guess))