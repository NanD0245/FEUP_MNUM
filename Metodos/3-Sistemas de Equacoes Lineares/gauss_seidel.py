def gauss_seidel(m1,m2,guess):
    dim = len(m1)
    for z in range(4):
        guess_copy = guess.copy()
        for i in range(dim):
            a1 = 0
            a2 = 0
            for j in range(dim):
                if (j < i):
                    a1 += m1[i][j]*guess[j]
                elif (i < j):
                    a2 += m1[i][j]*guess_copy[j]
            guess[i] = (m2[i] - a1 - a2) / m1[i][i]
        
    return guess

solution = [3.05769, 1.29807, 1.78846]

a = [[7,2,0], [4,10,1],[5,-2,8]]

b = [24,27,27]

print("SOLUTION: \n", solution, "\n")

print(gauss_seidel(a,b,[0,0,0]))