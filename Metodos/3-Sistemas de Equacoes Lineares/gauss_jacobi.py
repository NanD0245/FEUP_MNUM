def gauss_jacobi(m1,m2,guess):
    dim = len(m1)
    
    for z in range(4):
        guess_copy = guess.copy()
        for i in range(dim):
            a = 0
            for j in range(dim):
                if (j != i):
                    a += m1[i][j]*guess_copy[j]
            guess[i] = (m2[i]-a) / m1[i][i]
            
    return guess

solution = [3.05769, 1.29807, 1.78846]

a = [[7,2,0], [4,10,1],[5,-2,8]]

b = [24,27,27]

print("SOLUTION: \n", solution, "\n")

print(gauss_jacobi(a,b,[0,0,0]))