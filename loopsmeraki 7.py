a=1
b=3
while a<=5:
    guess=int(input("enter number 1 to 10"))
    a=a+1
    if guess==b:
        print(" guessed right")
        break
else:
    print("loses the game")