class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head==None:
            print("empty LinkedList")
        else:
            p=self.head

            while p:
                print(p.data)
                p=p.next
    
    def addnewnode(self,value):
        new=Node(value)

        if not self.head:
            self.head=new

        else:
            p=self.head
            while p.next is not None:
                p=p.next
            p.next=new

    def addnewnodeatindex(self,value,index):
        new=Node(value)

        if not self.head:
            print("This List is Empty hence adding the newnode at first")
            self.head=new
        else:
            p=self.head
            q=p
            count=0
            while p.next:
                count+=1
                p=p.next
            
            if count<index:
                print(" The index at which you want to add the node doesn't exist")
            else:
                for i in range (1,index-1):
                    q=q.next
                temp = q.next
                q.next=new
                new.next=temp
                


if __name__== "__main__":
    list=LinkedList()

    list.addnewnode(4)
    list.addnewnode(5)
    list.addnewnode(6)
    list.addnewnode(7)

    list.addnewnodeatindex(3,3)
    list.display()
