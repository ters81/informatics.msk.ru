# Задача №257. Конь
# https://informatics.msk.ru/mod/statements/view3.php?id=276&chapterid=257#1

# Требуется определить, бьет ли конь, стоящий на клетке с указанными координатами (номер строки и номер столбца),
# фигуру, стоящую на другой указанной клетке.
#
# Входные данные
# Вводятся четыре числа: координаты коня и координаты другой фигуры. Все координаты - целые числа в интервале от 1 до 8.
#
# Выходные данные
# Программа должна вывести слово YES, если конь может побить фигуру за 1 ход, в противном случае вывести слово NO.
#
# Примеры
# входные данные
# 1
# 1
# 3
# 2
# выходные данные
# YES
# входные данные
# 1
# 1
# 3
# 3
# выходные данные
# NO


a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

print('YES' if ((abs(a1 - b1) == 1 and abs(a2 - b2) == 2) or (abs(a2 - b2) == 1 and abs(a1 - b1) == 2)) else 'NO')
