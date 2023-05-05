 #square printing
n=5
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# for i in range(n):
#     for j in range(n):
#         print("*",end="  ")
#
#     print()


#Triangle pattern

# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end ="  ")
#     print()
#

#Decreasing triangle

# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *


# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end="  ")
#     print()


  #         *
  #       * *
  #     * * *
  #   * * * *
  # * * * * *

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#
#     print()



 # * * * * *
 #   * * * *
 #     * * *
 #       * *
 #         *

# n= 5
# for i in range(n):
#     for j in range(i+1):
#         print("-",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()


 #         *
 #       * * *
 #     * * * * *
 #   * * * * * * *
 # * * * * * * * * *


# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("_",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()







 # * * * * * * * * *
 #   * * * * * * *
 #     * * * * *
 #       * * *
 #         *


n=5
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n-1):
        print("*", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()
    