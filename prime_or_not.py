temp=0
n=int(input("Enter the value")) #2
for i in range(2,n):
    if n%i==0:
        temp=1
        break
if temp==1:
    print("Not prime")
else:
    print("Prime")
