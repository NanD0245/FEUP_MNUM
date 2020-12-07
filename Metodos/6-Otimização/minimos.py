def f(x):
    return x**4

def min(x0,h,f):
    x = 0
    count = 0
    while(1):
        x = x0 + h
        if (count == 0 and f(x0)-f(x) < 0):
            h = -h
        elif (f(x0) - f(x) >= 0):
            x0 = x
        elif (f(x0)-f(x) < 0):
            print(count)
            if h<0:
                print("[",x,",",x0-h,"]")
            else:
                print("[",x,",",x0+h,"]")
            break
        count += 1
    
        
min(2,0.001,f)