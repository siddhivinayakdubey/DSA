#include "iostream"
using namespace std;

class Node{
public:
    int data;
    Node *next;
};

Node* newNode(int x){
    Node* temp=new Node();
    temp->data=x;
    temp->next=NULL;
    return temp;
}

int Delete(int pos,Node* f)
{
    Node *p=f,*q=NULL;
    if(pos==1){
        q=p->next;
        int l=p->data;


        Node *r=q;
        while(r!=NULL){
            cout<<r->data;
            r=r->next;
        }
    }
    else{
        for(int i=0;i<pos-1;i++){
            q=p;
            p=p->next;
        }

        q->next=p->next;
        int x=p->data;
        delete p;

        Node *r=f;
        while(r!=NULL){
            cout<<r->data;
            r=r->next;
        }

}}


int main(){
    Node* f;
    f= newNode(5);
    f->next= newNode(6);
    f->next->next= newNode((8));

    Node* y=f;

    delete(2,f);

}