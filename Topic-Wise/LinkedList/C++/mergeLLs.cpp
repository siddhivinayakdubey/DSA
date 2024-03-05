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

int main(){
    Node* f=newNode(2);
    f->next=newNode(8);
    f->next->next= newNode(10);
    f->next->next->next= newNode(15);

    Node* s=newNode(4);
    s->next=newNode(7);
    s->next->next= newNode(12);
    s->next->next->next= newNode(14);


    Node *t=NULL, *last=NULL;

    //// Sabse pehle dekho ki dono list mai pehla element kiska comparative chhota hai
    //// or use hee third list ka sbse pehle element assign krddo saath hee mai ek or pointer banao tird naam ka
    //// or use bhi chhote element ke saath chalate raho

    if(f->data<s->data){
        t=last=f;
        f=f->next;
        last->next=NULL;
    }
    else{
        t=last=s;
        s=s->next;
        last->next=NULL;
    }


    while(f!=NULL && s!=NULL){

        if(f->data<s->data){
            last->next=f;
            last=f;
            f=f->next;
            last->next=NULL;
        }
        else{
            last->next=s;
            last=s;
            s=s->next;
            last->next=NULL;
        }

    }

    if(f!=NULL){
        last->next=f;
    }
    else{
        last->next=s;
    }



    while(t!=NULL){
        cout<<t->data<<" ";
        t=t->next;
    }
}