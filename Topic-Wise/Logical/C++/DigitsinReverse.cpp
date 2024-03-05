//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include "iostream"
using namespace std;
int main() {
    int n,r;
    cin>>n;

    while(n>0){
        r=n%10;
        n=n/10;
        cout<<r;

    }

}
