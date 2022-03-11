A = [[1, 2, 3, 4],
     [3, 0, 2, 1],
     [2, -1, 5, 1]]

for k in range(0, 2):
    for i in range(k+1, 3):
        pivot = A[i][k]/A[k][k]
        for j in range(0, 4):
            A[i][j] = A[i][j] - pivot * A[k][j]

print("Reduced matrix is: ", A)
