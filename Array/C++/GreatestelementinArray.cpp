//
// Created by Siddhivinayak Dubey on 27/08/21.
//

#include "iostream"
using namespace std;

int main(){
    int A[7]={4,8,6,9,5,2,7};
    int max=0;

    for(int i=0;i<7;i++){
        if(A[i]>max){
            max=A[i];
        }
    }
    cout<<max<<endl;
}