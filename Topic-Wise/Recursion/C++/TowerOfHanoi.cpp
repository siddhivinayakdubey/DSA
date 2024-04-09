//
// Created by Siddhivinayak Dubey on 09/04/24.
//
#include "iostream"
using namespace std;

void TOH(int n, string S, string H, string D){
    if (n==1){
        cout<<"Transfer Disk: "<< n << " from: "<<S<<" to: "<<D<<" via: "<<H<<endl;
        return;
    }
    TOH(n-1, S, D, H);
    cout<<"Transfer Disk: "<< n << " from: "<<S<<" to: "<<D<<" via: "<<H<<endl;
    TOH(n-1, H, S, D);
}

int main(){
    TOH(3, "s", "h", "d");
}