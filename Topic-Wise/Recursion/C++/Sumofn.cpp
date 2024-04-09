//
// Created by Siddhivinayak Dubey on 09/04/24.
//

#include "iostream"
using namespace std;

int sum = 0;
void sumofn(int x){
    if(x != 0){
        sum+=x;
        sumofn(x-1);
    }
    else{
        cout<<sum;
    }
}

int main(){
    sumofn(5);
}