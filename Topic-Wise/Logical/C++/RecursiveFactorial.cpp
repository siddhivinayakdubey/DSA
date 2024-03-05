//
// Created by Siddhivinayak Dubey on 08/09/21.
//

#include "iostream"
using namespace std;

int fact(int n){
    if(n==0)
        return 1;
    else
        return fact(n-1)*n;
}
int main(){
    cout<<fact(5);
}