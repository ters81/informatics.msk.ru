a = int(input())
b = int(input())
c = int(input())

if (a+b)>c and (b+c)>a and (a+c)>b and a>0 and b>0 and c>0:
    print('YES')
else:
    print('NO')
