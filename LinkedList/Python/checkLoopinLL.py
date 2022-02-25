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





    def checkloop(self):
        if self.head is None:
            print("Empty linked list")
        else:
            p=q=self.head
            while p and q is not None:
                p=p.next
                if( q.next.next is not None):
                    q=q.next.next
                else:
                    print("No loop")
                    return False


                if (p==q):
                    print("loop exists")
                    return True

            return False




if __name__ == '__main__':
    link=LinkedList()
    a=Node(8)
    a.next=Node(5)
    a.next.next=Node(4)
    a.next.next.next=Node(7)
    a.next.next.next.next.next=Node(9)
    a.next.next.next.next.next.next=a.next.next
    link.head=a
    print(link.checkloop())



