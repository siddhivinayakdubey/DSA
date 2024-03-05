//
// Created by Siddhivinayak Dubey on 23/09/21.
//

#include "iostream"
using namespace std;

class Node{
public:
    int data;
    Node* next;
};


Node* newNode(int k){
    Node* temp= new Node();
    temp->data=k;
    temp->next=NULL;
    return temp;
}

int main(){
    Node* f=newNode(3);
    f->next=newNode(5);
    f->next->next= newNode(5);
    f->next->next->next= newNode(8);
    f->next->next->next->next= newNode(8);
    f->next->next->next->next->next= newNode(8);

    Node *p=f, *q=p->next;

    while(q!=NULL){
        if(p->data!=q->data){
            p=q;
            q=q->next;
        }
        else{
            p->next=q->next;
            cout<<q->data<<" dupilcate value"<<endl;
            q=p->next;
        }
    }
}