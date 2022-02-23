//
// Created by Siddhivinayak Dubey on 27/08/21.
//

#include "iostream"
using namespace std;
int main(){
    int A[10],n=10;
    for(int i=0;i<n;i++){
        cin>>A[i];
    }
    for(int x:A){
        cout<<x<<" ";
    }

    //search for index of 12

    for(int i=0;i<10;i++){
        if(A[i]==12){
            cout<<"The Index position is: "<<i<<endl;
        }
    }

}
