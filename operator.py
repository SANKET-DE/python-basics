a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
d=int(input("Enter value of d:"))

e1=a+b*c**d
e2=(a+b)*c//d
e3=a//b+a%b*c**d
e4=(a>b)and(c<d)or(a!=b)
e5=(a&b)|(c^d)
e6=(a<<2)+(b>>1)

print("Expression 1:",e1)
print("Expression 2:",e2)
print("Expression 3:",e3)
print("Expression 4:",e4)
print("Expression 5:",e5)
print("Expression 6:",e6)