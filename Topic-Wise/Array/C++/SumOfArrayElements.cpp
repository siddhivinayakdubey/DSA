//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include "iostream"
using namespace std;

int main(){
    int sum=0,sum2=0,A[7]={4,8,6,9,5,2,7};
    for(auto x:A){
        sum+=x;
    }
    cout<<sum<<endl;

    for(int i=0;i<7;i++){
        sum2+=A[i];
    }
    cout<<sum2<<endl;
}
