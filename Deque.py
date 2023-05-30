class deque:
    def __init__(self,length):
        self.l=[None]*length
        self.length=length
        self.front=-1
        self.rear=-1
    def PushAtFront(self,data):
        if ((self.front==0 and self.rear==self.length-1) or (self.front==self.rear+1)):
            print("Deque Is Full")
        elif(self.front==-1 and self.rear==-1):
            self.front=self.rear=0
            self.l[self.front]=data
        elif(self.front==0):
            self.front=self.length-1
            self.l[self.front]=data
        else:
            self.front-=1
            self.l[self.front]=data
    def PushAtRear(self,data):
        if ((self.front==0 and self.rear==self.length-1) or (self.front==self.rear+1)):
            print("Deque Is Full")
        elif(self.front==-1 and self.rear==-1):
            self.front=self.rear=0
            self.l[self.rear]=data
        elif(self.rear==self.length-1):
            self.rear=0
            self.l[self.rear]=data
        else:
            self.rear+=1
            self.l[self.rear]=data
    def Display(self):
        i=self.front
        while(i!=self.rear):
            if(self.l[i]!=None):
                print(self.l[i])
            i=(i+1)%self.length
        print(self.l[self.rear])
    def PopAtFront(self):
        if(self.front==-1 and self.rear==-1):
            print("Deque Is Empty")
        elif(self.front==self.rear):
            self.l[self.front]=None
            self.front=self.rear=-1
        elif(self.front==self.length-1):
            self.l[self.front]=None
            self.front=0
        else:
            self.l[self.front]=None
            self.front+=1
    def PopAtRear(self):
        if(self.front==-1 and self.rear==-1):
            print("Deque Is Empty")
        elif(self.front==self.rear):
            self.l[self.rear]=None
            self.front=self.rear=-1
        elif(self.rear==0):
            self.l[self.rear]=None
            self.rear=self.length-1
        else:
            self.l[self.rear]=None
            self.rear-=1
length=int(input("Enter The Size Of The Deque: "))
Deque=deque(length)
print("1.PushAtFront\n2.PushAtRear\n3.PopAtFront\n4.PopAtEnd\n5.Display\n0.Exit\n")
while True: 
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        element=int(input("Enter The Element: "))
        Deque.PushAtFront(element)
    elif choice==2:
        element=int(input("Enter The Element: "))
        Deque.PushAtRear(element)
    elif choice==3:
        Deque.PopAtFront()
    elif choice==4:
        Deque.PopAtRear()
    elif choice==5:
        Deque.Display()
    elif choice==0:
        break
    else: 
        print("Enter A Valid Option")
print("Program Terminated")