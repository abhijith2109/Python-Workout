import math

def primefactors(n): #18
    #even number divisible
    while n%2==0:
        print(2) #2
        n=n//2 #9
    #n became odd
    for i in range (3,int(math.sqrt(n))+1,2): #3 - 4

        while n%i==0: #9%3
            print(i) #3 3
            n=n//i
    if n>2:
        print(n)
        print("....")

n=int(input("Enter the number for caluculating the prime factors"))
primefactors(n)