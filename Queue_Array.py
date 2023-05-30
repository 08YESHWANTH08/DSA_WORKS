import numpy
class Queue:
    def __init__(self,length):
        self.length=length
        self.queue=numpy.zeros(length,dtype='int')
        self.front=self.rear=-1
    def Enqueue(self,data):
        if (self.length-1)==self.rear:
            print("Queue Is Full")
            return
        elif(self.front==-1):
            self.front=self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear+=1
            self.queue[self.rear]=data
    def Dequeue(self):
        if (self.front==-1):
            print("Queue Is Empty")
        elif (self.front==0 and self.rear==0):
            self.front=self.rear=-1
        else:
            self.rear-=1
    def Is_Empty(self):
        if (self.front==-1):
            return True
        else:
            return False
    def Front(self):
        if (self.front==-1):
            return "Queue Is Empty"
        else:
            return self.queue[self.front]
    def Rear(self):
        if (self.front==-1):
            return "Queue Is Empty"
        else:
            return self.queue[self.rear]
    def Display(self):
        if (self.front==-1):
            print("Queue Is Empty")
        else:
            for i in range(self.rear+1):
                self.queue[i]
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


        
