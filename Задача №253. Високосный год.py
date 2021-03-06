# Задача №253. Високосный год
# https://informatics.msk.ru/mod/statements/view3.php?id=276&chapterid=253#1

# Требуется определить, является ли данный год високосным. (Напомним, что год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.)
#
# Входные данные
# Вводится единственное число - номер года (целое, положительное, не превышает 30000).
#
# Выходные данные
# Требуется вывести слово YES, если год является високосным и NO - в противном случае.
#
# Примеры
# входные данные
# 2007
# выходные данные
# NO

# входные данные
# 2000
# выходные данные
# YES


a = int(input())

print('YES' if ((a%4==0 and a%100!=0) or a%400==0) else 'NO')