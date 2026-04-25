m = int(input("Rows kitni?: "))
n = int(input("Columns kitne?: "))

matrix = []
for i in range(m):
    row = []
    for j in range(n):
        val = int(input(f"Row {i+1}, Col {j+1}: "))
        row.append(val)
    matrix.append(row)

for i in range(m):
    print(f"Sum of row {i+1} =", sum(matrix[i]))
