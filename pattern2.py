n = int(input("Enter the value of N: " ))
if (n%2==0):
	n=n//2
	n=2*(n-1)
	print(n//2)
else:
	n=(n//2)+1
	n=(n*2)+1
	print(n)
	