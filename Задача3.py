class NotANumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


result_list = []
while True:
    value = input('Ведите число или N для выхода: ')

    if value == 'N':
        print(f'Список {result_list}')
        break

    try:
        if not value.isnumeric():
            raise NotANumberException('NaN!')
        result_list.append(int(value))
    except NotANumberException as error:
        print('Вы ввели не число')