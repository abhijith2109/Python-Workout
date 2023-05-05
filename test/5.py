grp_of_values = [1, 5, 8, 3]
print(grp_of_values)
flag = 1
find_val =int(input("Enter a value"))
for i in grp_of_values:
    if i == find_val:
        flag = 2
    else:
        flag = 1

if flag == 2:
    print("True")
elif(flag==1):

    print("False")
