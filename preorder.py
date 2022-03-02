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

    def preorderiter(self):
        if self.root is None:
            print("Empty Tree")
        else:
            p=self.root
            stack=deque()

            while len(stack) or p is not None:
                if p is not None:
                    print(p.data)
                    stack.append(p)
                    p=p.lchild
                else:

                    p=stack.pop()
                    p=p.rchild




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
    print("""""")
    tree.preorderiter()