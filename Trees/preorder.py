from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

class Tree:
    def __init__(self):
        self.root=None



    def preorder(self):
        self.preorderecursion(self.root)


    def preorderecursion(self, p):
        if p is not None:
            print(p.data)
            self.preorderecursion(p.lchild)
            self.preorderecursion(p.rchild)


if __name__ == '__main__':
    root = Node(8)
    root.lchild = Node(3)
    root.lchild.lchild = Node(4)
    root.lchild.rchild = Node(9)
    root.rchild = Node(5)
    root.rchild.lchild = Node(7)
    root.rchild.rchild = Node(2)

    tree=Tree()
    tree.root=root
    tree.preorder()