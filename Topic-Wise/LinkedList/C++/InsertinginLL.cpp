//
// Created by Siddhivinayak Dubey on 18/09/21.
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
    f->next=newNode(7);
    f->next->next= newNode(9);
    f->next->next->next= newNode(15);
    f->next->next->next->next= newNode(20);

//    while(f!=0){
//        cout<<f->data<<" ";
//        f=f->next;
//    }
//    cout<<endl;

    Node* k= newNode(18);

    Node *p=f, *q=NULL;

    while(p->data<k->data){
        q=p;
        p=p->next;
    }
    k->next=q->next;
    q->next=k;
    Node* w=f;

    while(w!=0){
        cout<<w->data<<" ";
        w=w->next;
    }


}