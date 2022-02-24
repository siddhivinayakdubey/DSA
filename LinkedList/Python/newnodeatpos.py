class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def newnode(self,new):
        newnode=Node(new)
        if self.head is None:
            self.head=newnode
        else:
            p=self.head
            while p.next is not None:
                p=p.next
            p.next=newnode

    def newnodeatpos(self,pos,new):
        newnode=Node(new)
        p=self.head

        for i in range(0,pos-2):
            p=p.next
        newnode.next=p.next
        p.next=newnode

    def display(self):
        if self.head is None:
            print("Empty linked list")
        else:
            p=self.head

            while p is not None:
                print(p.data)
                p=p.next



if __name__ == '__main__':
    link = LinkedList()
    link.newnode(5)
    link.newnode(6)
    link.newnode(8)

    link.newnodeatpos(3,7)

    link.display()



