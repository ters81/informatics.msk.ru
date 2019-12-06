n = int(input())
m = int(input())
a = m//n
b = m%n
c = n-b
d = abs(c//n-1)
print(a+d)
