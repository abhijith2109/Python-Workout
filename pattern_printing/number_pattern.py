
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# n=5
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     print()
#     p=p+1

# 0
# 2 2
# 4 4 4
# 6 6 6 6
# 8 8 8 8 8

# n=5
# p=0
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     print()
#     p=p+2

# 2
# 1 1
# 2 2 2
# 1 1 1 1
# 2 2 2 2 2

# n=5
#
# for i in range(n):
#     for j in range(i+1):
#         if i%2 ==0:
#             print("2",end=" ")
#         else:
#             print("1",end=" ")
#     print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=5
#
# for i in range(n):
#     p = 1
#     for j in range(i+1):
#         print(p,end=" ")
#         p=p+1
#     print()


  # 1 2 3 4 5
  #   1 2 3 4
  #     1 2 3
  #       1 2
  #         1
  #

# n=5
# for i in range(n):
#     p=1
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#
#         print(p,end=" ")
#         p=p+1
#     print()


 # 5 4 3 2 1
 #   4 3 2 1
 #     3 2 1
 #       2 1
 #         1


# n=5
# k=5
# for i in range(n):
#     p=k
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(p,end=" ")
#         p=p-1
#     k=k-1
#     print()


  #         1
  #       1 2 1
  #     1 2 3 2 1
  #   1 2 3 4 3 2 1
  # 1 2 3 4 5 4 3 2 1

n=5

for i in range(n):
    for j in range(i,n):
        p=1
        print(" ",end=" ")
    for j in range(i):
        print(p,end=" ")
        p=p+1
    for j in range(i+1):
        print(p,end=" ")
        p=p-1
    print()
