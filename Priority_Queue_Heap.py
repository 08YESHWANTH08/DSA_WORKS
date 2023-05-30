class P_Q:
    def __init__(self,length):
        self.length=length
        self.size=-1
        self.l=[None]*self.length
    def parent(self,i):
        return (i-1)//2
    def left(self,i):
        return (2*i)+1
    def right(self,i):
        return (2*i)+2
    def swap(self,a,b):
        a,b=b,a
    def insert(self,data):
        self.size+=1
        self.l[self.size]=data
        self.shiftup(self.size)
    def shiftup(self,i):
        while (i>0 and self.l[self.parent(i)]<self.l[i]):
            self.swap(self.parent(i),i)
        i=self.parent(i)
    def remove(self,i):
        self.l[i]=self.l[0]+1
        self.shiftup(i)
        self.extractmax()
    def extractmax(self):
        temp=self.l[0]
        self.l[0]=self.l[self.size]
        self.size-=1
        self.shiftdown(0)
        return temp
    def shiftdown(self,i):
        max_index=i
        l=self.left(i)
        if(i<=self.size and self.l[l]>self.l[max_index]):
            max_index=l
        r=self.right(i)
        if(i<=self.size and self.l[r]>self.l[max_index]):
            max_index=r
        if(i!=max_index):
            self.swap(i,max_index)
            self.swiftdown(max_index)
    def display(self):
        for i in range(self.size+1):
            print(self.l[i],end=" ")
pq=P_Q(5)
for i in range(5):
    pq.insert(i)
pq.display()