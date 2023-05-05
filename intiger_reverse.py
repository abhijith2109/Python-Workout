num=int(input("Enter  Number"))
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10

print(rev)

# for loop method
# num=input("Enter  Number")
# rev=""
# for i in range(len(num),0,-1):
#     rev=rev+num[i-1]
# print(rev)