class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def newnodeatbegin(self,new):
        newnode=Node(new)
        newnode.next=self.head
        self.head=newnode

    def display(self):
        if self.head is None:
            print("Empty linked list")
        else:
            p=self.head

            while p is not None:
                print(p.data)
                p=p.next



if __name__ == '__main__':
    link=LinkedList()
    link.newnodeatbegin(5)
    link.newnodeatbegin(6)
    link.newnodeatbegin(8)

    link.display()


