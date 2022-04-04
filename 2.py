 #Write a C program to find the sum of the following series:
#2+5+8+11+14+ ........ upto N terms

n = int(input("enter the nth term: "))
sum = 0
for i in range(2, n+1):
    print(i)
    sum = sum + i
    i = i+3

print("The sum is: ", sum)