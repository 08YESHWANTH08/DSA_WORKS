class Node:
    #initialising a node
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class LinkedList:
    #declaring an empty DLL
    def __init__(self):
        self.head=None
        self.tail=None
    #inserting data at the front of DLL
    def PushAtFront(self,data):
        temp=self.head
        new_node=Node(data)
        #if DLL is empty
        if temp==None:
            #still inserting the data
            self.head=new_node
            self.tail=new_node
            new_node.next=self.tail
            new_node.prev=self.head
        else:
            temp.prev=new_node
            new_node.next=temp
            self.head=new_node    
            new_node.prev=self.tail   
    def PushAtMiddle(self,middle,data):
        temp=self.head
        new_node=Node(data)
        #if DLL is empty
        if temp==None:
            #still inserting the data
            self.head=new_node
            self.tail=new_node
            new_node.next=self.tail
            new_node.prev=self.head
        elif middle==0:
            temp.prev=new_node
            new_node.next=temp
            self.head=new_node    
            new_node.prev=self.tail   
        #if DLL is Not empty, traverse to specified Node (middle)
        else:
            while(middle>0):
                temp=temp.next
                middle-=1
            #creating new node with given data
            new_node=Node(data)
            if temp.next==self.tail:
                self.tail=new_node
                new_node.prev=temp
                temp.next=new_node
                new_node.next=self.head
            #assigning the address pointed by middle node as address pointed by new data
            else:
                temp1=Node()
                temp1=temp.next
                new_node.next=temp1
                temp1.prev = new_node 
                temp.next=new_node
                new_node.prev=temp
    def PushAtEnd(self,data):
        temp=self.head
        new_node=Node(data)
        if temp is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=self.tail
            new_node.prev=self.head
        else:
            self.tail=new_node
            new_node.prev=temp
            temp.next=new_node
            new_node.next=self.head
    def PopAtFront(self):
        temp=self.head
        if temp is None:
            print("Linked List Is Empty")
            return
        else:
            temp1=Node()
            temp1=temp.next
            temp1.prev=self.tail
            self.head=temp1
            del temp
    def PopAtMiddle(self,middle):
        temp=self.head
        if temp is None:
            print("Linked List Is Empty")
            return
        elif middle==0:
            temp1=Node()
            temp1=temp.next
            temp1.prev=self.tail
            self.head=temp1
            del temp
        else:
            while(middle>0):
                temp=temp.next
                middle-=1
            if temp==self.tail:
                temp1=Node()
                temp1=temp.prev
                temp1.next=self.head
                self.tail=temp1
                del temp
            else:
                temp1=Node()
                temp2=Node()
                temp1=temp.prev
                temp2=temp.next
                temp1.next=temp2
                temp2.prev=temp1
                del temp
    def PopAtEnd(self):
        temp=self.head
        #if there is not elements
        if temp is None:
            print("Linked List Is Empty")
        #if there is only one element
        elif temp==self.tail:
            self.head=None
            self.tail=None
            del temp
        else:
            if temp==self.tail:
                temp1=Node()
                temp1=temp.prev
                temp1.next=self.head
                self.tail=temp1
                del temp
            else:
                temp1=Node()
                temp2=Node()
                temp1=temp.prev
                temp2=temp.next
                temp1.next=temp2
                temp2.prev=temp1
                del temp
    def Search(self,key):
        temp=self.head
        if temp is None:
            return "Linked List Is Empty"
        while temp is not None:
            if key==temp.data:
                #returns true if key is in linked list
                return f"{key} Is In The Linked List"
            temp=temp.next
        #returns false if key is not in linked list
        return f"{key} Is Not In The Linked List"
    def Display(self):
        temp=self.head
        if self.head==self.tail:
            print("Linked List Is Empty")
            return
        while (temp!=self.tail):
            print(temp.data)
            #moving to next node
            temp=temp.next
        print(temp.data)
    def rDisplay(self):
        temp=self.tail
        if temp is None:
            print("Linked List Is Empty")
        else:    
            while (temp):
                print(temp.data)
                temp=temp.prev
l=LinkedList()
print("0.Exit\n1.PushAtFront\n2.PushAtMiddle\n3.PushAtEnd\n4.PopAtFront\n5.PopAtMiddle\n6.PopAtEnd\n7.Search\n8.Display\n9.RearDisplay\n")
while True: 
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        element=int(input("Enter The Element: "))
        l.PushAtFront(element)
    elif choice==2:
        element=int(input("Enter The Element: "))
        middle=int(input("Enter The Index: "))
        l.PushAtMiddle(middle,element)
    elif choice==3:
        element=int(input("Enter The Element: "))
        l.PushAtEnd(element)
    elif choice==4:
        l.PopAtFront()
    elif choice==5:
        Index=int(input("Enter The Index: "))
        l.PopAtMiddle(Index)
    elif choice==6:
        l.PopAtEnd()
    elif choice==7:
        key=int(input("Enter The Element To Search: "))
        print(l.Search(key))
    elif choice==8:
        l.Display()
    elif choice==9:
        l.rDisplay()
    elif choice==0:
        break
    else: 
        print("Enter A Valid Option")
print("Program Terminated")