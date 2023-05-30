class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def insert(node,key):
    if node is None:
        return Node(key)
    elif node.key>key:
        node.left=insert(node.left,key)
    elif node.key<key:
        node.right=insert(node.right,key)
    return node
def inorderprint(root):
    if root is not None:
        inorderprint(root.left)
        print(f"->{root.key}",end="")
        inorderprint(root.right)
root=Node(100)
insert(root,30)
insert(root,20)
insert(root,10)
inorderprint(root)