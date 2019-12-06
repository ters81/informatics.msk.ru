a = input()
b = a.find('h')
c = a.rfind('h')
d = a[:b]
e = a[(c+1):]
print (d+e)
