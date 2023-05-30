import numpy
class Stack:
    def __init__(self,length):
        self.stack=numpy.zeros(length,dtype=int)
        self.top=-1
        self.length=length
    def Push(self,data):
        if self.top==(self.length-1):
            print("Stack Is Full")
        else:
            self.top+=1
            self.stack[self.top]=data
    def Pop(self):
        if self.top==-1:
            print("Stack Is Empty")
        else:
            self.top-=1
    def Is_empty(self):
        if self.top==-1:
            return True
        else:
            return False
    def Top(self):
        if self.top==-1:
            return"Stack Is Empty"
        else:
            return self.stack[self.top]
    def Display(self):
        if self.top==-1:
            print("Stack Is Empty")
        else:
            for i in range(self.top+1):
                print(self.stack[i])
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
