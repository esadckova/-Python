class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data1 = input("Введите делимое: ")
inp_data2 = input("Введите делитель: ")
try:
    inp_data1 = int(inp_data1)
    inp_data2 = int(inp_data2)
    if inp_data2 == 0:
        raise OwnError("Делить на ноль нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    data = inp_data1 / inp_data2
    print(f"Все хорошо. Ваше число: {data}")
