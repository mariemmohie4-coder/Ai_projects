import ast

def matsum(matrix1, matrix2):
    if rows1 != rows2 or cols1 != cols2:
        print("Matrices dimensions do not match")
        return None
    result = []
    for i in range(rows1):
        r = []
        for j in range(cols1):
            r.append(matrix1[i][j] + matrix2[i][j])
        result.append(r)
    return result


def matsub(matrix1, matrix2):
    if rows1 != rows2 or cols1 != cols2:
        print("Matrices dimensions do not match")
        return None
    result = []
    for i in range(rows1):
        r = []
        for j in range(cols1):
            r.append(matrix1[i][j] - matrix2[i][j])
        result.append(r)
    return result


def matmul(matrix1, matrix2):
    if cols1 != rows2:
        print("Matrices cannot be multiplied: incompatible dimensions")
        return None
    result = []
    for i in range(rows1):
        r = []
        for j in range(cols2):
            s = 0
            for k in range(cols1):
                s += matrix1[i][k] * matrix2[k][j]
            r.append(s)
        result.append(r)
    return result


def scalarsum(scalar, matrix1):
    result = []
    for i in range(rows1):
        r = []
        for j in range(cols1):
            r.append(scalar + matrix1[i][j])
        result.append(r)
    return result


def scalarmul(scalar, matrix1):
    result = []
    for i in range(rows1):
        r = []
        for j in range(cols1):
            r.append(scalar * matrix1[i][j])
        result.append(r)
    return result


def matnorm(matrix1):
    all_values = []
    for i in range(rows1):
        for j in range(cols1):
            all_values.append(matrix1[i][j])

    min_val = min(all_values)
    max_val = max(all_values)

    if max_val == min_val:
        result = []
        for i in range(rows1):
            r = []
            for j in range(cols1):
                r.append(0)
            result.append(r)
        return result

    result = []
    for i in range(rows1):
        r = []
        for j in range(cols1):
            r.append((matrix1[i][j] - min_val) / (max_val - min_val))
        result.append(r)

    return result


import ast

print("Operations:")
print("1 - Matrix Sum")
print("2 - Matrix Subtraction")
print("3 - Matrix Multiplication")
print("4 - Scalar Addition")
print("5 - Scalar Multiplication")
print("6 - Normalization")

choice = input("Enter the operation number: ")

if choice == "1":
    text1 = input("Enter matrix 1 = ")
    text2 = input("Enter matrix 2 = ")
    matrix1 = ast.literal_eval(text1)
    matrix2 = ast.literal_eval(text2)

    rows1 = len(matrix1)
    rows2 = len(matrix2)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])

    result = matsum(matrix1, matrix2)
    print("Result =", result)

elif choice == "2":
    text1 = input("Enter matrix 1 = ")
    text2 = input("Enter matrix 2 = ")
    matrix1 = ast.literal_eval(text1)
    matrix2 = ast.literal_eval(text2)

    rows1 = len(matrix1)
    rows2 = len(matrix2)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])

    result = matsub(matrix1, matrix2)
    print("Result =", result)

elif choice == "3":
    text1 = input("Enter matrix 1 = ")
    text2 = input("Enter matrix 2 = ")
    matrix1 = ast.literal_eval(text1)
    matrix2 = ast.literal_eval(text2)

    rows1 = len(matrix1)
    rows2 = len(matrix2)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])

    result = matmul(matrix1, matrix2)
    print("Result =", result)

elif choice == "4":
    text1 = input("Enter matrix 1 = ")
    scalar = float(input("Enter scalar = "))
    matrix1 = ast.literal_eval(text1)

    rows1 = len(matrix1)
    cols1 = len(matrix1[0])

    result = scalarsum(scalar, matrix1)
    print("Result =", result)

elif choice == "5":
    text1 = input("Enter matrix 1 = ")
    scalar = float(input("Enter scalar = "))
    matrix1 = ast.literal_eval(text1)

    rows1 = len(matrix1)
    cols1 = len(matrix1[0])

    result = scalarmul(scalar, matrix1)
    print("Result =", result)

elif choice == "6":
    text1 = input("Enter matrix 1 = ")
    matrix1 = ast.literal_eval(text1)

    rows1 = len(matrix1)
    cols1 = len(matrix1[0])

    result = matnorm(matrix1)
    print("Result =", result)
