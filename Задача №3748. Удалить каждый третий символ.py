a = input()

n = len(a)

b =''

for i in range(n):
    if i%3!=0:
        b=b+a[i]
print(b)
