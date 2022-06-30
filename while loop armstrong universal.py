n=input("enter number")
i=0
armstrong=0
num=len(n)
while i<len(n):
    b=n[i]
    c=(int(b)**num)
    armstrong=c+armstrong
    i=i+1
print(armstrong)
if int(n)==armstrong:
    print("armstrong number")
else:
    print("not armstrong number")    