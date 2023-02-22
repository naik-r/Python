def Tower(n,source,desti,aux):
    if n==1:
        print("move disk 1 from source",source,"to destination",desti)
        return
    Tower(n-1,source,aux,desti)
    print("move disk",n,"From source",source,"to destination",desti)
    Tower(n-1,aux,desti,source)
n=3
Tower(n,'a','b','c')
