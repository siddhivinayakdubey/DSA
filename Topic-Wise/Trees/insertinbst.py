class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree:
    def __init__(self):
        self.root = None

    def bstinsertion(self, data):
        newnode = Node(data)

        if self.root is None:
            self.root = newnode
        else:
            p = self.root
            while p:
                if data == p.data:
                    print("not possible try it again")
                    break
                if data > p.data:
                    if p.rchild:
                        p = p.rchild
                    else:
                        p.rchild = newnode
                        break
                if data < p.data:
                    if p.lchild:
                        p = p.lchild
                    else:
                        p.lchild = newnode
                        break

    def bstinsertiontailing(self, data):
        newnode = Node(data)

        if self.root is None:
            self.root = newnode
        else:
            p = self.root
            while p:
                r = p
                if data == p.data:
                    print("not possible try it again")
                    break
                if data > p.data:
                    p = p.rchild
                if data < p.data:
                    p = p.lchild

    def inorder(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.inorderstart(self.root)

    def inorderstart(self, p):
        if p is not None:
            self.inorderstart(p.lchild)
            print(p.data)
            self.inorderstart(p.rchild)


if __name__ == '__main__':
    tree = Tree()
    tree.bstinsertion(5)
    tree.bstinsertion(9)
    tree.bstinsertion(1)
    tree.bstinsertion(6)
    tree.inorder()
