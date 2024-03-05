//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include "iostream"
using namespace std;

int main(){
    int i,n;
    cin>>n;
    for(i=1;i<=n;i++){
        if(n%i==0){
            cout<<i<<" ";
        }
    }
    return 0;
}
