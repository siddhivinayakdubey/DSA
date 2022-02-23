//
// Created by Siddhivinayak Dubey on 27/08/21.
//

#include "iostream"
using namespace std;

int main() {
    int n, count=0;
    cin>>n;
    for(int i=1;i<n;i++){
        if(n%i==0){
            count++;
        }
    }
    if(count<=2){
        cout<<"The no. "<<n<<" is prime";
    }
    else{
        cout<<"The no. "<<n<<" is not prime";
    }
}