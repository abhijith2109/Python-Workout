
i=0
result=0
n=int(input("Enter Number")) #153
number1 = n
temp = n

while (n!=0):
    n=n//10 #15 #1 #0
    i=i+1 #0+1=1 +1=2 +1 =3
while number1!=0:
    n=number1%10 #3 ,#5 ,#1
    result=result+pow(n,i) #27, 27+125=152 , 152+1=153
    number1=number1//10 #15,#1
if result==temp:
    print("Amstrong")
else:
    print("Not Amstrong")

