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
        self.preorderecursion(self.root)
    def preorderecursion(self,p):
        if p is not None:
            print(p.data)
            self.preorderecursion(p.lchild)
            self.preorderecursion(p.rchild)



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


