//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include "iostream"
using namespace std;

int main(){
    int A[10]={0,1,2,3,4,5,6,7,8,9};

    for(int x:A){
        cout<<x<<" ";
    }
    cout<<endl;
    for(int i=0;i<=10;i++){
        cout<<A[i];
    }

}
