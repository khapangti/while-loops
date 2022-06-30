n=int(input("enter number"))
p=0
i=1
while i<=n:
    if n%i==0:
        p=p+1
    i=i+1
if p==2:
    print("prime number")
else:
    print("not prime number")