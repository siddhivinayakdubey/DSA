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
        self.recursiverecursion(None,self.head)


    def recursiverecursion(self,q,p):
        if p is not None:
            self.recursiverecursion(p,p.next)
            p.next=q
        else:
            self.head=q







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



    def checkloop(self):
        if self.head is None:
            print("Empty linked list")
        else:
            p = q = self.head
            while p and q is not None:
                p = p.next
                if (q.next.next is not None):
                    q = q.next.next
                else:
                    print("No loop")
                    return False

                if (p == q):
                    print("loop exists")
                    return True

            return False



if __name__ == '__main__':
    list=LinkedList()
    list.newnode(5)
    list.newnode(8)
    list.newnode(4)
    list.newnode(7)
    list.newnodeatbegin(1)
    list.newnodeatpos(3,9)
    list.recursionshow()





