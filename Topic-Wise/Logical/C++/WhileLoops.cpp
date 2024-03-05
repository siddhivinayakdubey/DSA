//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include "iostream"
using namespace std;

int main(){
    int i=1,n=10;

    while(i<=n){
        cout<<i<<endl;
        i++;
    }

    do{
        cout<<i;
        i++;
    } while (i<=n);
}
