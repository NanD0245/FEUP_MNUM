from math import sqrt

def f(x):
    return 2 * x ** 2 - 5 * x - 2


def f1(x):
    return (2 / 5) * x ** 2 - (2 / 5)


def f2(x):
    return (5 / 2) + (1 / x)


def f3(x):
    return sqrt((5 / 2) * x + 1)


def f4(x):
    return -sqrt((5 / 2) * x + 1)

def picard_peano(f,guess):
    max_iter = 50
    num_iter = 0
    prev_guess = guess + 1
    while (abs(guess-prev_guess) > 1e-5 and num_iter <= max_iter):
        prev_guess = guess
        guess=f(guess)
        num_iter += 1
    return guess


guess = float(input("INITIAL GUESS: "))

print(picard_peano(f1, guess))

guess = float(input("INITIAL GUESS: "))

print(picard_peano(f2, guess))

guess = float(input("INITIAL GUESSasd: "))

print(picard_peano(f3, guess))

#guess = float(input("INITIAL GUESS: "))

#print(picard_peano(f4, guess))


