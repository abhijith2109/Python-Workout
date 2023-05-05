
arr=[1,44,5,2,44,5,6,1,8,9]
new_arr=[]
print(arr)
for i in arr:
    if i not in new_arr:
        new_arr.append(i)
print(new_arr)


