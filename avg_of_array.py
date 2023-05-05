# arr=[]
# size=int(input("Enter the size of the array"))
# for i in range (0,size):
#     ele=int(input("Enter the index value of ,"+str(i)+":"))
#     arr.append(ele)
#
# avg=sum(arr)/size
#
# print(avg)

arr=[]
def avg(size):
    for i in range (0,size):
        ele=int(input("Enter the index value of"+str(i)+":"))
        arr.append(ele)
    return sum(arr)/size
size=int(input("Enter the size"))
res=avg(size)
print(res)
