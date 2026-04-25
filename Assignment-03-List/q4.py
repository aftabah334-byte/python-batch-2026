lst = []
n = int(input("Kitne elements?: "))
for i in range(n):
    lst.append(int(input(f"Element {i+1}: ")))

last = lst[-1]
for i in range(len(lst)-1, 0, -1):
    lst[i] = lst[i-1]
lst[0] = last

print("Rotated list:", lst)
