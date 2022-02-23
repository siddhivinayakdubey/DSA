////
//// Created by Siddhivinayak Dubey on 13/09/21.
////
//
//#include "iostream"
//using namespace std;
//
//class Node{
//public:
//    int data;
//    Node* next;
//};
//
//void Display(Node* p){
//    if(p!=NULL){
//        Display(p->next);
//        cout<<p->data;
//
//    }
//}
//int main(){
//    Node *head=NULL,*second=NULL,*third=NULL,*q;
//
//    head=new Node();
//    second=new Node();
//    third= new Node();
//
//    head->data=1;
//    head->next=second;
//
//    second->data=2;
//    second->next=third;
//
//    third->data=3;
//    third->next=NULL;
//
//    q=head;
//    int count=0;
//    Display(q);
//
//    while(q!=NULL){
//        count++;
//        cout<<q->data;
//        q=q->next;
//    }

//    cout<<endl<<count<<endl;
//    cout<<head;


#include "iostream"
using namespace std;

class Node{
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
    Node* p= newNode(8);
    p->next= newNode(7);
    p->next->next= newNode(6);

    Node* q=p;
    while (q!=0){
        cout<<q->data;
        q=q->next;
    }


}


