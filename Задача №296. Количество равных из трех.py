a = int(input())
b = int(input())
c = int(input())

if a==b==c:
    print('3')
elif (a==b and a!=c and b!=c) or (a==c and a!=b and b!=c) or (c==b and a!=b and b!=a):
    print('2')
else:
    print('0')
