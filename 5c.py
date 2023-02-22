def Wordcount(str):
 counts=dict()
 words=str.split()
 for word in words:
        if word in counts:
             counts[word]+=1
        else:
             counts[word]=1
 return counts
string=input("enter the string:")
print(Wordcount(string))
