# Write a Python program to remove duplicates from a list
lst=[1,2,3,4,5,4,6,6,1]
print("List=",lst)
lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)

print("New list after removing duplicates",lst2)