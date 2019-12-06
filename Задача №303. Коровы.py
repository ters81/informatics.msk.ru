n = int(input())

a = str(n)
x = a[-1]


if 5<=n<=19:
    print(a+' '+'korov')
    
elif int(x)==0 or 5<=int(x)<=9:
    print(a+' '+'korov')

elif 2<=int(x)<=4:
    print(a+' '+'korovy')

elif int(x)==1:
    print(a+' '+'korova')
