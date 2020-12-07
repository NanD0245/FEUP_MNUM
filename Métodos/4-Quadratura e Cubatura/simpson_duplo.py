def simpson_duplo(matriz, hx, hy):
    integral = 0
    for i, z_line in enumerate(matriz):
        for j, z in enumerate(z_line):
            if (i == 0 and (j == 0 or j == 2)) or (i == 2 and (j == 0 or j == 2)):
                integral += z
            elif (j == 1 and (i == 0 or i == 2)) or (i == 1 and (j == 0 or j == 2)):
                integral += 4*z
            else:
                integral += 16*z
    return ((hx*hy)/9) * integral

matriz = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

print(simpson_duplo(matriz, 1, 1))