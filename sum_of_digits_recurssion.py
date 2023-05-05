def sum_of_digit(n):   #22
    if n==0:
        return 0
    return (n%10+ sum_of_digit(int(n//10))) #2+2

n=int(input("Enter digits"))
ans=sum_of_digit(n)
print("sum of digit :",ans)