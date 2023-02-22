l=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    ele=[input(),int(input()),int(input())]
    l.append(ele)
    mydict={i:l[i] for i in range(len(l))}
print(mydict)
