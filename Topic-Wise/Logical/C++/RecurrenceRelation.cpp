//
// Created by Siddhivinayak Dubey on 08/09/21.
//

#include "iostream"
using namespace std;
int fun(int n){
    static int x=0;
    if(n>0){
        int y=fun(n-1)+x;

    }
    return 0;
}

int main(){
    fun(5);
}