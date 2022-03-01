from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

class Tree:
    def __init__(self):
        self.root=None

    def levelorderiter(self):
        queue=deque()
        p=self.root
        queue.append(p)

        while queue[0] is not None:
            p=queue.popleft()
            print(p.data)
            queue.append(p.lchild)
            queue.append(p.rchild)


if __name__ == '__main__':
    tree = Tree()
    root = Node(8)
    root.lchild = Node(3)
    root.lchild.lchild = Node(4)
    root.lchild.rchild = Node(9)
    root.rchild = Node(5)
    root.rchild.lchild = Node(7)
    root.rchild.rchild = Node(2)

    tree.root = root
    tree.levelorderiter()


