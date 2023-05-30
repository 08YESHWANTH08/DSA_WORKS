class Binary_Tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def insert(self,data):
        if self.data==None:
            self.data=data
        else:
            if data<self.data:
                if self.left==None:
                    self.left=Binary_Tree(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right==None:
                    self.right=Binary_Tree(data)
                else:
                    self.right.insert(data)
    def delete(self,data):
        
def Inorderprint(root):
    if root is None:
        return
    Inorderprint(root.left)
    print(f"{root.data}",end=" ")
    Inorderprint(root.right)
def Preorderprint(root):
    if root is None:
        return
    print(f"{root.data}",end=" ")
    Preorderprint(root.left)
    Preorderprint(root.right)
def Postorderprint(root):
    if root is None:
        return
    print(f"{root.data}",end=" ")
    Postorderprint(root.right)
    Postorderprint(root.left)
root=Binary_Tree('g')
root.insert('c')  
root.insert('b')  
root.insert('a')  
root.insert('e')  
root.insert('d')  
root.insert('f')  
root.insert('i')  
root.insert('h')  
root.insert('j')  
root.insert('k') 
Inorderprint(root)
print()
Preorderprint(root)
print()
Postorderprint(root)