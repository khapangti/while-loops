n=int(input("enter number"))
f=1
s=1
i=1
while i<=n:
    f=f*i
    s=s+1/f
    i=i+1
print(s,"+",f,"/",i,"!","+",end=" ")