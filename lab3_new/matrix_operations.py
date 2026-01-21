def matrix_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] 
            for i in range(len(a))]

def matrix_sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] 
            for i in range(len(a))]

# Input matrices
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

print("Enter Matrix A:")
mat1 = [list(map(int, input().split())) for _ in range(rows)]
print("Enter Matrix B:")
mat2 = [list(map(int, input().split())) for _ in range(rows)]

add_result = matrix_add(mat1, mat2)
sub_result = matrix_sub(mat1, mat2)

print("Matrix A:", mat1)
print("Matrix B:", mat2)
print("A + B:", add_result)
print("A - B:", sub_result)
