class Cir_Q:
    def __init__(self,length):
        self.length=length
        self.l=[0]*self.length
        self.front=-1
        self.rear=-1
    def Push(self,data):
        if(self.front==-1 and self.rear==-1):
            self.front=self.rear=0
            self.l[self.front]=data
        elif((self.rear+1)%self.length==self.front):
            print("List Is Full")
        else:
            self.rear=(self.rear+1)%self.length
            self.l[self.rear]=data
    def Pop(self):
        if(self.front==-1 and self.rear==-1):
            print("List Is Empty")
        elif(self.front==0 and self.rear==0):
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.length
    def Display(self):
        if(self.front==-1 and self.rear==-1):
            print("List Is Empty")
        else:
            i=self.front
            while(i!=self.rear):
                print(self.l[i])
                i=(i+1)%self.length
            print(self.l[self.rear])
length=int(input("Enter The Size Of The cir_q: "))
cir_q=Cir_Q(length)
print("1.Push\n2.Pop\n3.Display\n0.Exit\n")
while True: 
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        element=int(input("Enter The Element: "))
        cir_q.Push(element)
    elif choice==2:
        cir_q.Pop()
    elif choice==3:
        cir_q.Display()
    elif choice==0:
        break
    else: 
        print("Enter A Valid Option")
print("Program Terminated")
