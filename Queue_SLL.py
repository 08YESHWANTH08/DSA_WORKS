class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None
class Queue:
    def __init__(self,length):
        self.head=None
        self.top=-1
        self.length=length
    def Enqueue(self,data):
        if self.top==(self.length-1):
            print("Queue Is Full")
        else:
            new_node=Node(data)
            if self.head is None:
                self.head=new_node
            else:
                new_node.next=self.head
                self.head=new_node
            self.top+=1
    def Dequeue(self):
        temp=self.head
        if temp is None:
            print("Queue Is Empty")
            return
        elif temp.next is None:
            self.head=None
        else:
            while (temp.next.next is not None):
                temp=temp.next
            del temp.next
            temp.next=None
        self.top-=1
    def Is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    def Front(self):
        if self.head is None:
            return"Queue Is Empty"
        else:
            return self.head.data
    def Rear(self):
        if self.head is None:
            return"Queue Is Empty"
        else:
            temp=self.head
            while (temp.next is not None):
                temp=temp.next
            return temp.data
    def Display(self):
        temp=self.head
        if temp is None:
            print("Queue Is Empty")
        else:
            while(temp):
                print(temp.data)
                temp=temp.next
length=int(input("Enter The Size Of The Queue: "))
Queue=Queue(length)
print("1.Enqueue\n2.Dequeue\n3.Is_empty\n4.Front\n5.Rear\n6.Display\n0.Exit\n")
cond='y'
while cond.lower()=='y': 
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        element=int(input("Enter The Element: "))
        Queue.Enqueue(element)
    elif choice==2:
        Queue.Dequeue()
    elif choice==3:
        print(Queue.Is_empty())
    elif choice==4:
        print(Queue.Front())
    elif choice==5:
        print(Queue.Rear()) 
    elif choice==6:
        Queue.Display()
    elif choice==0:
        break
    else: 
        print("Enter A Valid Option")
print("Program Terminated")
