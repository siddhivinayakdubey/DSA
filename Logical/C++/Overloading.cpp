//
// Created by Siddhivinayak Dubey on 01/09/21.
//
#include "iostream"
using namespace std;

//int max(int x,int y){
//    return x>y?x:y;
//}

int max(int x=0,int y=0,int z=0){
    return x>y && x>z ? x : y>z ? y : z;
}
int main(){
    int c= max(10,12);
    int b=max(10,12,19);
    int a=max();
    cout<<c<<endl;
    cout<<b<<endl;
    cout<<a<<endl;
}