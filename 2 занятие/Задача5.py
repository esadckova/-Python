a = float(input("Введите число рейтинга"))
b = [7, 5, 3, 3, 2]
i = 0
for element in b:
    if a <= element:
        i += 1
    else:
        break
b.insert(i, a)
print(b)
