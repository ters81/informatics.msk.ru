n = int(input())
a = n//60
b = n%60
c = n//1440
d = a - 24*c
print(d, b)
