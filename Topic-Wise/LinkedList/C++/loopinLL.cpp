//
// Created by Siddhivinayak Dubey on 24/09/21.
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
int isLoop(Node *f){
    Node *p=NULL,*q=NULL;
    p=q=f;

    do{
        p=p->next;
        q=q->next;
        q= q!=NULL?q->next:NULL;
    } while(p&&q);
    return p==q? true:false;
}
int main(){
    Node* f=newNode(2);
    f->next=newNode(8);
    f->next->next= newNode(10);
    f->next->next->next= newNode(15);
    f->next->next->next->next= f->next->next;

    cout<<isLoop(f);

}
