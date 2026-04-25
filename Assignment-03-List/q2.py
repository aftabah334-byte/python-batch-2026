lst = []
n = int(input("Kitne elements?: "))
for i in range(n):
    lst.append(int(input(f"Element {i+1}: ")))

reversed_lst = []
for i in range(len(lst)-1, -1, -1):
    reversed_lst.append(lst[i])

print("Reversed list:", reversed_lst)
