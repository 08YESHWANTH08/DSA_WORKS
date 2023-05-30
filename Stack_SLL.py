class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None
class Stack:
    def __init__(self,length):
        self.head=None
        self.top=0
        self.length=length
    def Push(self,data):
        if self.top==self.length:
            print("Stack Is Full")
        else:
            new_node=Node(data)
            self.top+=1
            if self.head is None:
                self.head=new_node
            else:
                new_node.next=self.head
                self.head=new_node
    def Pop(self):
        temp=self.head
        if temp is None:
            print("Stack Is Empty")
        elif temp.next is None:
            self.head=None
        else:
            self.head=temp.next
            del temp
        self.top-=1
    def Is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    def Top(self):
        if self.head is None:
            return"Stack Is Empty"
        else:
            return self.head.data
    def Display(self):
        temp=self.head
        if temp is None:
            print("Stack Is Empty")
        else:
            while(temp):
                print(temp.data)
                temp=temp.next
length=int(input("Enter The Size Of The Stack: "))
stack=Stack(length)
print("1.Push\n2.Pop\n3.Is_empty\n4.Top\n5.Display\n0.Exit\n")
cond='y'
while cond.lower()=='y': 
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        element=int(input("Enter The Element: "))
        stack.Push(element)
    elif choice==2:
        stack.Pop()
    elif choice==3:
        print(stack.Is_empty())
    elif choice==4:
        print(stack.Top())
    elif choice==5:
        stack.Display()
    elif choice==0:
        break
    else: 
        print("Enter A Valid Option")
print("Program Terminated")
