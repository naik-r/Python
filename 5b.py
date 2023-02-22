n=int(input("Enter the length of list:"))
f=[]
for i in range(n):
       j=input("Enter the element:")
       f.append(j)
print("List of elements are:",f)
t=[]
Nfor i in f:
      if i not in t:
         t.append(i)

print("After removing the duplicates:",t)
