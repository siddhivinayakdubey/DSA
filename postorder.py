from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None


class Tree:
    def __init__(self):
        self.root=None

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
    def postorderiter(self):
        if self.root is None:
            print("Empty list")
        else:
            p=self.root
            stack=deque()

            while len(stack) or p is not None:
                if p is not None:
                    stack.append(p)
                    p=p.lchild
                else:
                    temp=stack.pop()
                    if temp>0:
                        stack.append(-temp)
                        p=temp.rchild
                    else:
                        print(temp.data)
                        temp=None



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
    tree.postorderiter()