a=10
b=20
c=30

a=a+b
b=a-b
a=a-b

b,c=c,b

d=a+b+c
e=d/3

print("a =",a)
print("b =",b)
print("c =",c)
print("d =",d)
print("e =",e)

print(d>e*2)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))