n=int(input("entr the number:"))
a=0
b=1
c=0
while c<n:
    c=a+b
    a=b
    b=c

if c==n:
    print("given is fibonacci number: ",n)

else:
    print("given is not fibonacci number: ",n)
