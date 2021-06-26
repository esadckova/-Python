a = input("Введите несколько слов через пробел: ")
b = a.split(' ')
for ind, el in enumerate(b, 1):
    if len(el) > 10:
        el = el[0:10]
    print(ind, el)
