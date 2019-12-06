a = int(input())
b = int(input())
c = int(input())

A = [a,b,c]
A.sort()

x = A[0]
y = A[1]
z = A[2]

if a<=0 or b<=0 or c<=0:
    print('impossible')
elif (a+b<=c) or (a+c<=b) or (c+b<=a):
    print('impossible')
elif (x**2+y**2)==z**2:
    print('right')
elif (x**2+y**2)>z**2:
    print('acute')
else:
    print('obtuse')
