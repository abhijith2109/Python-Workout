
ll=int(input("Enter the lower limit"))
ul=int(input("Enter the upper limit"))
for n in range(ll,ul):
    i = 0
    result = 0
    number1 = n
    temp = n

    while (n != 0):
        n = n // 10  # 15 #1 #0
        i = i + 1  # 0+1=1 +1=2 +1 =3  #to get the no.of digit
    while number1 != 0:
        n = number1 % 10  # 3 ,#5 ,#1
        result = result + pow(n, i)  # 27, 27+125=152 , 152+1=153
        number1 = number1 // 10  # 15,#1
    if result == temp:

        print(result)
