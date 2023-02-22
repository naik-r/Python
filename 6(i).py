d=int(input("enter a decimal:"))
b=0
c=0
temp=d
while(temp>0):
    b=((temp%2)*(10**c)+b)
    temp=int(temp/2)
    c+=1
print("Binary of {x} is:{y}".format(x=d,y=b))
