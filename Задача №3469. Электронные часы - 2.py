n = int(input())
h = n//3600
m = n//60

h1 = h%24

m1 = m%60
m2 = m1//10
m3 = m1%10

s1 = n%60
s2 = s1//10
s3 = s1%10

print(h1,':',m2,m3,':',s2,s3,sep="")
