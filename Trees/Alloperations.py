from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

class Tree:
    def __init__(self):
        self.root=None


    def create(self):
        print("Enter the root data")
        data=input()
        rootnode=Node(data)
        self.root=rootnode
        list=deque()
        list.append(self.root)

        while len(list)!=0:
            p=list.popleft()
            print("Enter the left child to"+str(p.data)+"or -1 to pass")
            x=input()
            if(x!='-1'):
                t1=Node(x)
                p.lchild=t1
                list.append(t1)
                print(list)

            print("Enter the right child to"+str(p.data)+" or -1 to pass")
            x = input()
            if (x !='-1'):
                t2 = Node(x)
                p.rchild = t2
                list.append(t2)
                print(list)


    def preorder(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.preorderstart(self.root)
    def preorderstart(self,p):
        if p is not None:
            print(p.data)
            self.preorderstart(p.lchild)
            self.preorderstart(p.rchild)



    def inorder(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.inorderstart(self.root)
    def inorderstart(self,p):
        if p is not None:
            self.inorderstart(p.lchild)
            print(p.data)
            self.inorderstart(p.rchild)



    def postorder(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.postorderstart(self.root)
    def postorderstart(self,p):
        if p is not None:
            self.postorderstart(p.lchild)
            self.postorderstart(p.rchild)
            print(p.data)

    def levelorderiter(self):
        queue = deque()
        p = self.root
        queue.append(p)

        while queue[0] is not None:
            p = queue.popleft()
            print(p.data)
            queue.append(p.lchild)
            queue.append(p.rchild)




if __name__ == '__main__':
    tree=Tree()
    root=Node(8)
    root.lchild=Node(3)
    root.lchild.lchild=Node(4)
    root.lchild.rchild=Node(9)
    root.rchild=Node(5)
    root.rchild.lchild=Node(7)
    root.rchild.rchild=Node(2)

    tree.root=root
    tree.preorder()


