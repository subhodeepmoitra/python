n=int(input("Enter the value of n: "))
if (n%2==0):
    n=n//2
    print(3**(n-1))
else:
    n=(n//2)+1
    print(2**(n-1))
