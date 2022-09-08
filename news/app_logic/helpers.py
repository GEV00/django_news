def str_connector(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        return str1 + str2
    else:   
        return TypeError('Аргументы функции должны быть строками')


def numbers_devision(num1, num2):
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        return 'Аргументы должнв быть целыми или вещественными числами'
    if num2 != 0:
        return num1 / num2
    return 'На ноль делить нельзя'


def is_open(hour):
    if isinstance(hour, int):
        if 0 < hour < 25:
            if 13 <= hour < 14:
                return False
            if hour in range(8, 14) or hour in range(14, 20):
                return True
            else:
                return False
        raise ValueError('Агрумент должен быть положительным целым числом от 1 до 24')
    raise ValueError('Укажите час в качестве положительного целого числа от 1 до 24')