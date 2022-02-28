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




if __name__ == '__main__':
    tree=Tree()
    tree.create()


















# list=deque()
# list.append(4)
# list.append(5)
# list.popleft()
# print(list)
# print(len(list))