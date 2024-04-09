//
// Created by Siddhivinayak Dubey on 08/04/24.
//

#include "iostream"
using namespace std;

class Node{
public:
    int value;
    Node* next;
};

class SinglyLinkedList{
private:
    Node* head{nullptr};

public:
    explicit SinglyLinkedList() : head(nullptr) {}

    explicit SinglyLinkedList(int data) : head(nullptr){
        newnodeatbegin(data);
    }

    //Function to display the LinkedList
    void Display(){
        if (head == nullptr){
            cout<<"List is Empty"<<endl;
        }
        else{
            Node* q = head;
            while(q){
                cout<<q->value<<endl;
                q=q->next;
            }
        }
    }

    //Function to add a node at beginning
    void newnodeatbegin(int data){
        Node* newNode = new Node();
        newNode->value= data;
        newNode->next= nullptr;

        if(head == nullptr){
            head = newNode;
        }
        else{
            newNode->next=head;
            head=newNode;
        }
    }

    //Function to add a node at specific position
    void newnodeatpos(int data, int pos){
        if(pos==1){
            newnodeatbegin(data);
        }
        else{
            Node* newNode = new Node();
            newNode->value=data;
            newNode->next= nullptr;
            Node* q = head;
            while(pos>2){
                q = q->next;
                pos-=1;
            }
            newNode->next=q->next;
            q->next=newNode;
        }
    }

    //Function to add a new Node
    void newnodeatend(int data){
        Node* newNode = new Node();
        newNode->value=data;
        newNode->next= nullptr;

        if (head == nullptr){
            head = newNode;
        }
        else{
            Node* p = head;

            while(p->next){
                p = p->next;
            }
            p->next = newNode;
        }
    }

    //Reverse a Linked List
    void reverse(){
        if(head == nullptr){
            cout<<"Nothing in the list to reverse"<<endl;
        }
        else{
            Node* p = nullptr;
            Node* q = head;
            while(q){
                Node* r = q->next;
                q->next=p;
                p = q;
                q = r;
            }
            head = p;
        }
    }

    //Recursive Reverse
    void recursivereverse(){
        rechelp(nullptr, head);
    }

    void rechelp(Node* q, Node* p){
        if (p != nullptr){
            rechelp(p,p->next);
            p->next=q;
        }
        else{
            head = q;
        }
    }
};

int main(){
    SinglyLinkedList list1;
    list1.newnodeatend(6);
    list1.newnodeatend(7);
    list1.newnodeatend(11);
    list1.newnodeatend(2);
    list1.newnodeatpos(8, 5);
    list1.reverse();
    list1.recursivereverse();

    cout<<"boring, list1 starts"<<endl;
    list1.Display();

    SinglyLinkedList list2(3);
    list2.newnodeatbegin(4);
    list2.newnodeatbegin(1);
    cout<<"yay, list2 starts"<<endl;
    list2.Display();
}