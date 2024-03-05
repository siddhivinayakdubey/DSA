//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include<iostream>
using namespace std;
int main() {
    int a,b;

    cin>>a>>b;

    if(a>b && a>0){
        cout<<"Max is pisitive:"<<a<<endl;
    }
    else if(a<b || a>0){
        cout<<"Max is:"<<b<<endl;
    }

    if(a%2==0){
        cout<<"The number is even"<<endl;
    }
    else{
        cout<<"The number is odd"<<endl;
    }

    if(not a>0){
        cout<<"Hi";
    }
}
