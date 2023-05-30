class Node:
    def __init__(self,data=None,priority=None):
        self.data=data
        self.pr=priority
        self.next=None
class PQ:
    def __init__(self):
        self.head=None
    def insert(self,data,pr):
        new_node=Node(data,pr)
        if self.head==None:
            self.head=new_node
        else:
            if new_node.pr<self.head.pr:
                new_node.next=self.head
                self.head=new_node
            else:
                temp=self.head
                while temp.next:
                    if new_node.pr<=temp.next.pr:
                        break
                    temp=temp.next
                new_node.next=temp.next
                temp.next=new_node

    def pop(self):
        if self.head==None:
            print("Priority Queue Is Empty")
        else:
            self.head=self.head.next
    def display(self):
        temp=self.head
        if temp is None:
            print("Priority Queue Is Empty")
            return
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
pq=PQ()
pq.insert(10,3)
pq.insert(20,2)
pq.insert(30,1)
pq.display()
print()
pq.pop()
pq.display()
