n = int(input("Rows: "))
m = int(input("Columns: "))

print("Matrix A daalo:")
A = [[int(input(f"A[{i+1}][{j+1}]: ")) for j in range(m)] for i in range(n)]

print("Matrix B daalo:")
B = [[int(input(f"B[{i+1}][{j+1}]: ")) for j in range(m)] for i in range(n)]

print("Sum Matrix:")
for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i][j] + B[i][j])
    print(row)
