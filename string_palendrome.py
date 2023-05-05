# str=input("Enter a string")
# rev=str[::-1]
# print(rev)

def palein(str):
    rev=str[::-1] #slicing
    return rev
str=input("Enter a string")
ans=palein(str)
if ans==str:
    print(str,"is palendrome")
else:
    print(str,"not a palendrome")






