def enqueue(qu, n):
    qu.append(n)
    
def dequeue(qu):
    if(len(qu)==0):
        print("Queue Underflow")
    else:
        print("De-queued item: ", qu.pop(0))
        
queue = []

while True:
    print("1. Enqueue")
    print("2. De-queue")
    print("3. Display")
    print("4. Exit")
    
    ch = int(input("Enter choice: "))
    
    if(ch==1):
        n = int(input("Enter the value: "))
        enqueue(queue, n)
    elif(ch==2):
        dequeue(queue)
    elif(ch==3):
        print(queue)
    elif(ch==4):
        break