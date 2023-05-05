#
# def swap(n1,n2):
#     temp=n1
#     n1=n2
#     n2=temp
#     print("After swapping",n1,n2)
#
#
# n1=int(input("Enter first value"))
# n2=int(input("Enter second value"))
# print("Before swapping ",n1,n2)
# ans=swap(n1,n2)


# n1=int(input("Enter first value"))
# n2=int(input("Enter second value"))
# print("Before swapping ",n1,n2)
#
# n1,n2=n2,n1
# print("After swapping",n1,n2)



n1=int(input("Enter first value")) #2
n2=int(input("Enter second value"))#4
print("Before swapping ",n1,n2) #2 4

n1=n1-n2  #-2
n2=n1+n2  #2
n1=n2-n1

print("After swapping",n1,n2)
 
