# Задача №355. Симметричная ли матрица
# https://informatics.msk.ru/mod/statements/view3.php?id=282&chapterid=355

# Проверьте, является ли двумерный массив симметричным относительно главной диагонали. Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний.
#
# Входные данные
# Программа получает на вход число n $\leq$ 100, являющееся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по n чисел, являющихся элементами массива.
#
# Выходные данные
# Программа должна выводить слово yes для симметричного массива и слово no для несимметричного.
#
# Примеры
# входные данные
# 3
# 0 1 2
# 1 5 3
# 2 3 4
# выходные данные
# yes
# входные данные
# 3
# 0 0 0
# 0 0 0
# 1 0 0
# выходные данные
# no


n = int(input())

a = []

for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

s1 = 0
for i in range(n):
    for j in range(n):
        if i != j and a[i][j] == a[j][i]:
            s1 += 1

s2 = n**2 - n

if s1 == s2:
    print('yes')
else:
    print('no')