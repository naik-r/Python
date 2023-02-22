a=int(input("Enter the prize of the quantity:"))
if a<=2000:
     print("total=",a)
elif a>2000 and a<5000:
     c=a-((5/100)*a)
     print("total=",c)
elif a>5000 and a<10000:
     c=a-((10/100)*a)
     print("total=",c)
elif a>10000:
     c=a-((15/100)*a)
     print("total=",c)    
