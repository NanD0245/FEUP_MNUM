import math

def f1(x,y):
    return 2*x**2-x*y-5*x+1

def f2(x,y):
    # return x + 3 * (math.log(x) / math.log(10)) - y**2
    return x + 3 * math.log(x) - y**2

def df1x(x,y):
    return -y + 4*x -5
    
def df1y(x,y):
    return -x
    
def df2x(x,y):
    return 3/x + 1
    
def df2y(x,y):
    return -2*y

def jacobian(x,y):
    return df1x(x,y)*df2y(x,y) - df1y(x,y) * df2x(x,y)

def h(x,y):
    return (f1(x,y) * df2y(x,y) - f2(x,y) * df1y(x,y))/jacobian(x,y)

def k(x,y):
    return (f2(x,y) * df1y(x,y) - f1(x,y) * df2x(x,y))/jacobian(x,y)

def newton_sistemas(f1,f2,df1x,df1y,df2x,df2y):
    guess_x = 4
    prev_x = 4
    guess_y = 4
    prev_y = 4
    for i in range(100):
        guess_x = prev_x  - ((f1(prev_x,prev_y)*df2y(prev_x,prev_y) - f2(prev_x,prev_y)*df1y(prev_x,prev_y)) /
                           (df1x(prev_x,prev_y)*df2y(prev_x,prev_y) - df2x(prev_x,prev_y) * df1y(prev_x,prev_y)))
        guess_y = prev_y  - (((f2(prev_x,prev_y)*df1x(prev_x,prev_y) - f1(prev_x,prev_y)*df2x(prev_x,prev_y)) /
                        (df1x(prev_x,prev_y)*df2y(prev_x,prev_y) - df2x(prev_x,prev_y) * df1y(prev_x,prev_y))))
        prev_x = guess_x
        prev_y = guess_y
        #print(guess_x,guess_y)
    return (guess_x, guess_y)

print(newton_sistemas(f1, f2, df1x, df1y, df2x, df2y))

def g1(x,y):
    return math.sqrt((x*(y+5)-1)/2)

def g2(x,y):
    return math.sqrt(x+3*math.log(x))

def picard_peano_sistemas(g1,g2):
    guess_x = 4
    prev_x = 4
    guess_y = 4
    prev_y = 4
    for i in range(100):
        guess_x = g1(prev_x,prev_y)
        guess_y = g2(prev_x,prev_y)
        prev_x = guess_x
        prev_y = guess_y
    return (guess_x,guess_y)

print(picard_peano_sistemas(g1, g2))


# =============================================================================
# n sei o que isto faz
# guess_x = 4
# guess_y = 5
# old_x = 2
# old_y = 2
# 
# 
#     
# for i in range(40):
#     if (guess_x-old_x < 1e-5):
#         break
#     guess_x = old_x - h(old_x, old_y)
#     guess_y = old_y - k(old_x, old_y)
#     old_x = guess_x
#     old_y = guess_y
# 
# print(guess_x, guess_y)
# =============================================================================
