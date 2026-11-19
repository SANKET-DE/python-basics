
a=int(input("Enter the price of product 1:"))
b=int(input("Enter the price of product 2:"))
c=int(input("Enter the price of product 3:"))

d=int(input("Enter quantity of product 1:"))
e=int(input("Enter quantity of product 1:"))
f=int(input("Enter quantity of product 1:"))

g=int(input("Enter discount percent:"))
h=int(input("Enter GST percent:"))

p1=a*d
p2=b*e
p3=c*f

print(f"Product 1 total: {p1}")
print(f"Product 2 total: {p2}")
print(f"Product 3 total: {p3}")

subtotal=p1+p2+p3                                                                           

print(f"Subtotal: {subtotal}")

discount=(g/100)*subtotal

print(f"Discount amount: {discount}")

afterdiscount=subtotal-discount

print(f"Amount after discount: {afterdiscount}")

gst=(h/100)*afterdiscount

print(f"GST amount: {gst}")

finalamount=gst+afterdiscount

print(f"Final amount: {finalamount}")
