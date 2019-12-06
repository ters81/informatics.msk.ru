n = int(input())

x = n//60

if n-x*60>=35:
    x = x+1
    x1 = 0
    z1 = 0

else:
    x = n//60 
    y = 60*x
    z = n-y

    x1 = z//10
    y1 = 10*x1
    z1 = z-y1

a = z1*15 + x*440 + x1*125
b = x*440 + (x1+1)*125


if a<b:
    print(z1, x1, x)
else:
    print('0', x1+1, x)
