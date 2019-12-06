x = float(input())
y = float(input())
count = 0
if y>x:
    while x<=y:
        count+=1
        x=x*1.1
    print(count+1)
elif y<x:
    print('0')
else:
    print('1')
