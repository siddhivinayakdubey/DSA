//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include "iostream"
using namespace std;

int main(){
    int A[10]={6,8,13,17,20,22,25,28,30,35};
    int n=10;
    int key=22;
    int l=0,h=n;

    for (int i=l;i<h;i++){
        int m =(l+h)/2;
        if(key==A[m]){
            cout<<m<<endl;
            break;
        }
        else if(key>A[m]){
            l=m;
        }
        else if(key<m){
            h=m;
        }
    }
}
