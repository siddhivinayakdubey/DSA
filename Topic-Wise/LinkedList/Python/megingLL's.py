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


    def mergelists(self,list2):
        first=self.head
        second=list2.head

        if first.data<second.data:
            p=q=first
            first=first.next
        else:
            p=q=second
            second=second.next


        while first and second is not  None:

            if first.data<second.data:
                q.next=first
                first=first.next
                q=q.next
            else:
                q.next=second
                second=second.next
                q=q.next

        if first is not None:
            q.next=first
            q=q.next

        if second is not None:
            q.next=second
            q=q.next









if __name__ == '__main__':
    lis1=LinkedList()
    lis1.newnode(1)
    lis1.newnode(3)
    lis1.newnode(5)
    lis1.newnode(7)

    list2=LinkedList()
    list2.newnode(2)
    list2.newnode(4)
    list2.newnode(6)
    list2.newnode(8)


    list2.mergelists(lis1)
    lis1.display()

