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

    def display(self):
        if self.head is None:
            print("Empty linked list")
        else:
            p=self.head

            while p is not None:
                print(p.data)
                p=p.next



    def deletion(self,key):
        if self.head is None:
            print("No node to be deleted")
        elif (self.head.data==key):
            temp=self.head
            self.head=self.head.next
            temp=None
        else:
            p=self.head
            while p.next is not None and p.next.data!=key:
                p=p.next
            if p.next is None:
                print("there were no mathing elements to delete")
            else:
                temp=p.next
                p.next=p.next.next
                temp=None





if __name__ == '__main__':
    link=LinkedList()
    link.newnode(5)
    link.newnode(6)
    link.newnode(8)
    link.deletion(9)
    link.display()

