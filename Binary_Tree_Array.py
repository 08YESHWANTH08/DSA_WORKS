class Binary_Tree:
    def __init__(self,length):
        self.l=[None]*length
        self.length=length
        self.size=-1
    def insert(self,data):
        self.size+=1
        self.l[self.size]=data
    def delete(self,data):
        index=0
        flag=0
        for i in range(self.size):
            if (self.l[i]==data):
                index=i
                flag=1
                break
        if flag:
            self.l[i],self.l[self.size]=self.l[self.size],self.l[i]
            self.size-=1
            return
        print("Element Not Found")
    def display(self):
        for i in range(self.size+1):
            print(f"->{self.l[i]}",end="")
bt=Binary_Tree(5)
bt.insert(10)
bt.insert(20)
bt.insert(40)
bt.insert(30)
bt.insert(50)
bt.display()
print()
bt.delete(40)
bt.display()