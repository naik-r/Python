print("Enter the elements:")
print("press x to end the list:")
f=[]
c=input()
while(c!='x'):
      f.append(int(c))
      c=input()
for i in range(len(f)):
   for j in range (len(f)-1):
       if f[i]>f[j]:
         temp=f[i]
         f[i]=f[j]
         f[j]=temp

print(f)
