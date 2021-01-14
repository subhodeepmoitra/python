def linear_search(list , n):
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False

list = []
n = int(input("Number of terms: "))
for i in range (0,n):
    element = [input() , int(input())]
    list.append(element)
if linear_search (list , n):
    print("Found")
else:
    print("Not Found")