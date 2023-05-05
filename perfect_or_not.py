#6  1,2,3
# 1+2+3=6
 #6 is a perfect number


n=int(input("Enter a number"))
sum=0
for i in range(1,n//2+1): #4>1-3 =1,
    rem=n%i  #6%1=0
    if rem==0:
        sum=sum+i #i=1+2=3+3=6

if n==sum:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect")

