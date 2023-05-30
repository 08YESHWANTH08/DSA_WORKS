class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class CSLL:
    def __init__(self):
        self.tail=None
    def Push(self,middle,data):
        new_node=Node(data)
        if(self.tail==None):
            self.tail=new_node
            new_node.next=self.tail
        elif(middle==0):
            head=self.tail.next
            new_node=head
            self.tail.next=new_node
        else:
            for i in range(1,middle-1):
                head=head.next
            new_node.next=head.next
            if(head!=self.tail):
                head.next=new_node
            else:
                new_node.next=self.tail.next
                head.next=new_node
    def Pop(self,middle):
        head=Node()
        head=self.tail.next
        if(head==None):
            print("List Is Empty")
        elif middle==0:
            self.tail.next=head.next
            del head
        else:
            for i in range(1,middle-1):
                head=head.next
            temp=Node()
            temp=head.next
            if(head.next!=self.tail):
                head.next=temp.next
                del temp
            else:
                self.tail.next=temp.next
                del temp
    def Display(self):
        head=self.tail.next
        while(head!=self.tail):
            print(head.data)
            head=head.next
        print(head.data)
l=CSLL()
while True: 
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        element=int(input("Enter The Element: "))
        middle=int(input("Enter The Position: "))
        l.Push(middle,element)
    elif choice==2:
        position=int(input("Enter The Position: "))
        l.Pop(position)
    elif choice==3:
        l.Display()
    elif choice ==4:
        break
    else: 
        print("Enter A Valid Option")
print("Program Terminated")