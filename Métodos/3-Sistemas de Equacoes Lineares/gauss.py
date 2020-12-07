def gauss(aMatrix):
    
    print("Upper triangular, Solution\n")

    dimV = len(aMatrix)
    for diag in range(dimV):
        pivot = aMatrix[diag][diag]
        
        for col in range(dimV + 1):
            aMatrix[diag][col] /= pivot
            
        for lin in range(diag + 1, dimV):
            factor = aMatrix[lin][diag]
            
            for col in range(diag, dimV + 1):
                aMatrix[lin][col] -= aMatrix[diag][col] * factor
                
    for diag in range(dimV):
        print(aMatrix[diag])
        
    print("\nLower triangular, Solution:\n")
    
    for diag in range(dimV - 1, - 1, - 1):
        for lin in range(diag - 1, - 1, - 1):
            factor = aMatrix[lin][diag]
            for col in range(dimV, diag - 1, -1):
                aMatrix[lin][col] -= aMatrix[diag][col] * factor

    for diag in range(dimV):
        print(aMatrix[diag])
        
    return [aMatrix[x][dimV] for x in range(dimV)]


def residueSLE(aMatrix, solutionMatrix):
    dimV = len(aMatrix)

    resid = [0] * dimV
    for eq in range(dimV):
        for sol in range(dimV):
            resid[eq] += aMatrix[eq][sol] * solutionMatrix[sol]

        resid[eq] = aMatrix[eq][dimV] - resid[eq]

    print(resid)
    return resid



solution = [2, 1, 3]
m = [[3,6,9,39], [2,5,-2,3],
     [1,3,-1,2]]

print("SOLUTION: \n", solution, "\n")

solu = gauss(m)

print("\nNumerical Solution\n", solu, "\n")

print("\nSolution residue:\n")

res = residueSLE(m, solu)

print("\nSolution residue:\n", res, "\n")