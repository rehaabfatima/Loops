num=int(input("Enter a number to check"))

flag=False

if num>1:
    for i in range(2,num):
        if (num % i)==0:
         flag=True
         break
 
if flag:
    print("It is a not a prime number")
else:
    print("It is not a prime number")