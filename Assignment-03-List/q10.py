r1 = int(input("Matrix A ki rows: "))
c1 = int(input("Matrix A ke columns: "))
c2 = int(input("Matrix B ke columns: "))

print("Matrix A daalo:")
A = [[int(input(f"A[{i+1}][{j+1}]: ")) for j in range(c1)] for i in range(r1)]

print("Matrix B daalo:")
B = [[int(input(f"B[{i+1}][{j+1}]: ")) for j in range(c2)] for i in range(c1)]

result = [[0]*c2 for _ in range(r1)]
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j] += A[i][k] * B[k][j]

print("Result Matrix:")
for row in result:
    print(row)
