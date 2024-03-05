//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include "iostream"
using namespace std;

int main(){
    int m,n;
    cin>>m>>n;

    while(m!=n){
        if(m>n){
            m=m-n;
        }
        if(n>m){
            n=n-m;
        }
    }
    cout<<m;
    return 0;
}
