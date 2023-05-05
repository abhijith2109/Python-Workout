def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)


num=int(input("Enter the value"))
print("Factorial is",fact(num))
