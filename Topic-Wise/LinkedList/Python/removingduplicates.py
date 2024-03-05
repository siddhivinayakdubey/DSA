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


    def removingduplicates(self):
        array=[]
        if self.head is None:
            print("Empty List")

        elif self.head.next is None:
            print("Only one node")
        else:
            p=self.head
            array.append(p.data)
            while p.next is not None:
                if p.next.data in array:
                    temp=p.next
                    p.next=p.next.next
                    temp=None
                else:
                    array.append(p.next.data)
                    p = p.next






if __name__ == '__main__':
    link=LinkedList()
    link.newnode(5)
    link.newnode(8)
    link.newnode(5)
    link.newnode(8)
    link.removingduplicates()
    link.display()

