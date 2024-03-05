//
// Created by Siddhivinayak Dubey on 30/08/21.
//

#include "iostream"
using namespace std;

int main(){
    int A[5]={1,2,3,4,5};
    int *p=A,*q;
    q=&A[3];

    cout<<*q<<endl;
    cout<<q<<endl;

    p[0]=4;
    p[1]=5;
    p[2]=6;
    p[3]=7;
    cout<<*p+1<<endl;


    int *x;
    int y=10;
    x=&y;
    cout<<x<<endl;


}