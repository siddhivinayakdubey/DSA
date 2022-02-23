//
// Created by Siddhivinayak Dubey on 27/08/21.
//

#include "iostream"
#include "math.h"
using namespace std;
int main() {
    int n,r,sum=0,temp;
    cin>>n;
    temp=n;

    while(n>0){
        r=n%10;
        r= pow(r,3);
        sum+=r;
        n=n/10;
    }
    if(sum==temp){
        cout<<"It's an Armstrong number";
    }
    else{
        cout<<"It's not an Armstrong number";
    }

}