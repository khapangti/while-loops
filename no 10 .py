n=int(input('enter number'))
a=1
while a<=n//2:
    if n%2==0:
        print("not prime")
        break
    a=a+1
else:
    print("prime")