lst = []
n = int(input("Kitne elements?: "))
for i in range(n):
    lst.append(int(input(f"Element {i+1}: ")))

print("Alternate elements:")
for i in range(0, len(lst), 2):
    print(lst[i])
