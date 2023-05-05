num=[1,2,3,4]
num2=[]
flag=1
for i in num:
    if i not in num2:
        num2.append(i)
        flag=2
    else:
        flag=1


if flag==2:
    print("True")
else:
    print("False")
