a = input()

e1 = a.find('f')
e2 = a.find('f', e1+1)
a1 = '  '+a
b = a1.find('f')
c = a1.find('f', b+1)
x1 = int(b/abs(b))
x2 = int((1-x1)/2)
d = int((b+c)/abs(b+c))

print ((str(e2)*d)+('-2'*x2))
