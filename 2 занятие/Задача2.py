l = input("Введите несколько чисел через пробел: ")
a = l.split(' ')
inx = len(a) if len(a) % 2 == 0 else len(a) - 1
a[:inx:2], a[1:inx:2], = a[1:inx:2], a[:inx:2]
print("Новый", a)
