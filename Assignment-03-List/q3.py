lst = []
n = int(input("Kitne elements?: "))
for i in range(n):
    lst.append(int(input(f"Element {i+1}: ")))

largest = lst[0]
for num in lst:
    if num > largest:
        largest = num

print("Largest number:", largest)
