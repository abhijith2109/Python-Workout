num=int(input("Enter number"))
temp=num
while num>0:
    j=num%10
    if j!=0 and j!=1:
        print(temp,"is not a binary number")
        break
    else:
        num=num//10
        if num==0:
            print(temp,"is binary number")
