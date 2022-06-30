bin=int(input("enter number"))
dec=0
i=1
while bin!=0:
    rev=bin%10
    bin=bin//10
    dec=dec+rev*i
    i=i*2
print(dec)