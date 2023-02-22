import cmath
a=float(input("enter the number a:"))
b=float(input("enter the number b:"))
c=float(input("enter the number c:"))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print("the root1 is:",sol1)
print("the root2 is:",sol2)

      
      
