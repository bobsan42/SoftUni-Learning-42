matrix = []
for i in range(3):
    matrix.append([])
    for j in range(1, 4):
        matrix[i].append(j)


# Use Comprehensions

matrix = [[0 for j in range(2)] for i in range(3)]

matrix = [[j for j in range(1, 4)] for i in range(3)]

matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for sublist in matrix for num in sublist]
# [1, 2, 3, 4, 5, 6]