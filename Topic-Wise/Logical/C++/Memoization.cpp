//
// Created by Siddhivinayak Dubey on 09/09/21.
//
#include "iostream"
using namespace std;
int f[10];

int fib( int n){
    if(n<=1){
        f[n]=n;
        return n;
    }

    else{
        if(f[n-1]==-1)
            f[n-1]= fib(n-1);
        if(f[n-2]==-1)
            f[n-2]= fib(n-2);
        return f[n-1]+f[n-2];
    }
}

int main(){
    int x=7;
    for(int i=0;i<10;i++){
        f[i]=-1;
    }
    cout<<fib(x);
}