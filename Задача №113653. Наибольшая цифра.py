# Задача №113653. Наибольшая цифра
# https://informatics.msk.ru/mod/statements/view3.php?id=26735&chapterid=113653#1

# Дана строка, содержащая только десятичные цифры. Найти и вывести наибольшую цифру.
#
# Входные данные
# Вводится строка ненулевой длины. Известно также, что длина строки не превышает 1000 знаков и строка содержит только десятичные цифры.
#
# Выходные данные
# Выведите максимальную цифру, которая встречается во введенной строке.
#
# Примеры
# входные данные

# 11111111
# выходные данные
# 1



def stroka(s, maximum):
    if len(s) == 0:
        return maximum
    maximum = max(maximum, int(s[0]))
    return stroka(s[1::], maximum)


print(stroka(input(), maximum=0))