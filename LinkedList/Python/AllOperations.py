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

    def newnodeatbegin(self,new):
        newnode=Node(new)
        newnode.next=self.head
        self.head=newnode

    def countnodes(self):
        p=self.head
        count=0
        while p is not None:
            count+=1
            p=p.next
        print("The count is: "+str(count))

    def recursionshow(self):
        self.recursivehelp(self.head)


    def recursivehelp(self,p):
        if p is None:
            ("Empty")

        else:
            print(p.data)
            self.recursivehelp(p.next)


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

    def checksorted(self):
        if self.head is None:
            print("Empty List")

        if self.head.next is None:
            print("Only One node and hence it is sorted: " + self.head.data)

        else:
            p = self.head
            while p.next is not None:
                if p.data < p.next.data:
                    p = p.next
                else:
                    p = p.next
                    return False
            return True

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
    list=LinkedList()
    list.newnode(5)
    list.newnode(8)
    list.newnode(4)
    list.newnode(7)
    list.newnodeatbegin(1)
    list.newnodeatpos(3,9)
    list.recursionshow()





