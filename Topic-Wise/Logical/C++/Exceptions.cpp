//
// Created by Siddhivinayak Dubey on 03/09/21.
//
#include "iostream"
using namespace std;

int division(float x,float y){
    if(y==0)
        throw 1;
    else
        return (float) x/y;
}

int main(){
    float c;
    try{
        c=division(4.0,0);
        cout<<(float)c<<endl;
    }
    catch(int e){
        cout<<"exceptional case of denominator being zero caught";
    }
}

