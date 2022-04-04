def push(st, n):
    st.append(n)

def stack_pop(st):
    if (len(st)==0):
        print("Underflow")
    else:
        print("Popped: ", st.pop())

stack = []
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    
    ch = int(input("Enter choice: "))
    
    if(ch==1):
        n = int(input("Enter the value: "))
        push(stack, n)
        
    elif(ch==2):
        stack_pop(stack)
        
    elif(ch==3):
        print(stack)
        
    elif(ch==4):
        break