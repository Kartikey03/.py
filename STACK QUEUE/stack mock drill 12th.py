s=[]
def push(val):
    s.append(val)
    print("value pushed to stack")

def pop():
    if s==[]:
        print("Underflow")

    else:
        p= s.pop()
        print("value popped is ", p)

def display():
    if s==[]:
        print("underflow")
        return
    else:
        for i in range(len(s)-1,-1,-1):
            print(s[i])

while True:
    
    print("--------------STACK OPERATIONS----------------")

    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")
    ch=int(input("Enter your choice:"))
    if ch==1:
        val=int(input("Enter the value to be pushed to stack::"))
        push(val)
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        break
print("bye bye......")
   
