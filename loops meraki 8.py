a=1
b=5
while a<=5:
    guess=int(input("enter number"))
    a=a+1
    if guess<b:
        print("number entered by you is small, try another one")
    elif guess>b:
        print("number entered by you is greater,try one more time")
    elif guess==b:
        print("wow you gussed the correct number")
        break
else:
    print("none")