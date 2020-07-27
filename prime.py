def prime(n):
   if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
num = int(input("enter a positive number: "))
if (num > 0):
    prime(num)
else:
    print("I have told to enter a positive number: ")

