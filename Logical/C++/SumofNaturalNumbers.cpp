//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include <iostream>
using namespace std;

int main(){
    int n,sum,sum2=0;
    cin>>n;
    sum=(n*(n+1))/2;
    cout<<sum<<endl;

    for(int i=0;i<=n;i++){
        sum2+=i;

    }
    cout<<sum2;
    return 0;



}
