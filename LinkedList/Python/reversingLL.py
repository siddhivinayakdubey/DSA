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

    def reversingelements(self):
        array=[]
        if self.head is None:
            print("Empty List")
        else:
            p=self.head
            i=0
            while p is not None:
                array.append(p.data)
                i+=1
                p=p.next
            q=self.head
            while q is not None:
                i-=1
                q.data=array[i]
                q=q.next

    # SLIDING POINTERS
    def reversinglinks(self):
        if self.head is None:
            print("Empty List")
        else:
            p=self.head
            q=None
            r=None

            while p is not None:
                r=q
                q=p
                p=p.next
                q.next=r

            self.head=q

    # RECURSIVE REVERSE
    def revrecursionhelp(self):
        self.recursiverecusrion(None,self.head)


    def recursiverecusrion(self,q,p):
        if p is not None:
            self.recursiverecusrion(p,p.next)
            p.next=q
        else:
            self.head=q














if __name__ == '__main__':
    link=LinkedList()
    link.newnode(5)
    link.newnode(6)
    link.newnode(8)
    link.revrecursionhelp()
    link.display()



