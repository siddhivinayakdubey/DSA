class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    # From the previous code
    def newnode(self,new):
        newnode=Node(new)
        if self.head is None:
            self.head=newnode
        else:
            p=self.head
            while p.next is not None:
                p=p.next
            p.next=newnode

    def displaycircular(self):
        if self.head is None:
            print("Empty linked list")
        else:
            p=self.head
            flag=0
            while(p is not self.head or flag==0):
                flag=1
                print(p.data)
                p=p.next






if __name__ == '__main__':
    link = LinkedList()
    a = Node(8)
    a.next = Node(5)
    a.next.next = Node(4)
    a.next.next.next = Node(7)
    a.next.next.next.next = Node(1)
    a.next.next.next.next.next =Node(9)
    a.next.next.next.next.next.next = a
    link.head=a
    link.displaycircular()


