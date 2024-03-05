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

    def show(self):
        if self.head is None:
            print("Empty Linkedlist")
        else:
            p=self.head
            while p is not None:
                print(p.data)
                p=p.next




    def sortedinsertion(self,key):
        newnode=Node(key)
        if self.head is None:
            self.head=newnode

        if self.head.data>key:
            newnode.next=self.head
            self.head=newnode


        else:
            p=self.head

            while p.next.data<key:
                p=p.next
            newnode.next=p.next
            p.next=newnode



if __name__ == '__main__':
    link=LinkedList()
    link.newnode(5)
    link.newnode(7)
    link.newnode(8)
    link.newnode(10)
    link.newnode(18)

    link.sortedinsertion(1)
    link.show()


