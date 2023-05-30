class Node:
    #initialising a node
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    #declaring an empty SLL
    def __init__(self):
        self.head=None
    #inserting data at the front of SLL
    def PushAtFront(self,data):
        #creating a node for new data
        new_node=Node(data)
        #assigning the address pointed by head as address pointed by new data
        new_node.next=self.head
        #assigning the new data as head
        self.head=new_node
    def PushAtMiddle(self,middle,data):
        temp=self.head
        #if SLL is empty
        if temp is None:
            print("Linked List Is Empty")
            #still inserting the data
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
        elif middle==0:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node       
        #if SLL is Not empty, traverse to specified Node (middle)
        else:
            for i in range(1,middle-1):
                #assigning next Node as temp
                temp=temp.next
            #creating new node with given data
            new_node=Node(data)
            #assigning the address pointed by middle node as address pointed by new data
            new_node.next=temp.next
            #assigning the address pointed by middle node to the new data
            temp.next=new_node
    def PushAtEnd(self,data):
        #if SLL is empty
        if self.head is None:
            #creating new node
            new_node=Node(data)
            #pointing head to new node
            self.head=new_node
            return
        #assigning head as temp
        temp=self.head
        #if SLL is not empty
        while temp.next is not None:
            #traversing to the end Node
            temp=temp.next
        #creating a new node
        new_node=Node(data)
        #assigning address pointed by new node as NULL
        new_node.next=temp.next #temp=Last_node, temp.next=NULL
        #assigning address pointed by previous- end node as new node
        temp.next=new_node
    def PopAtFront(self):
        if self.head is None:
            print("Linked List Is Empty")
        #if linked list is not empty
        else:
            #assign head to address of node pointed by first node
            self.head=self.head.next
    def PopAtMiddle(self,middle):
        temp=self.head
        if temp is None:
            print("Linked List Is Empty")
            return
        if middle==0:
            self.head=self.head.next
            del temp
        else:
            for i in range(1,middle-1):
                temp=temp.next
            temp2=Node()
            temp2 = temp.next
            temp.next=temp2.next
            del temp2
    def PopAtEnd(self):
        #if there is not elements
        if self.head is None:
            print("Linked List Is Empty")
        #if there is only one element
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
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
        if temp is None:
            print("Linked List Is Empty")
            return
        while (temp):
            print(temp.data)
            #moving to next node
            temp=temp.next
l=LinkedList()
print("1.PushAtFront\n2.PushAtMiddle\n3.PushAtEnd\n4.PopAtFront\n5.PopAtMiddle\n6.PopAtEnd\n7.Search\n8.Display\n")
cond='y'
while cond.lower()=='y': 
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        element=int(input("Enter The Element: "))
        l.PushAtFront(element)
    elif choice==2:
        element=int(input("Enter The Element: "))
        middle=int(input("Enter The Position: "))
        l.PushAtMiddle(middle,element)
    elif choice==3:
        element=int(input("Enter The Element: "))
        l.PushAtEnd(element)
    elif choice==4:
        l.PopAtFront()
    elif choice==5:
        position=int(input("Enter The Position: "))
        l.PopAtMiddle(position)
    elif choice==6:
        l.PopAtEnd()
    elif choice==7:
        key=int(input("Enter The Element To Search: "))
        print(l.Search(key))
    elif choice==8:
        l.Display()
    else: 
        print("Enter A Valid Option")
    cond=input("Do want to continue ? (y/n): ")
print("Program Terminated")