//
// Created by Siddhivinayak Dubey on 09/09/21.
//
#include "iostream"
using namespace std;

int main(){
    int arr[10]={2,4,6,8,11,13,17,20,0};
    int n=8;
    arr[8]=14;
    n++;
//    for(int j=0;j<n;j++){
//        cout<<arr[j]<<",";
//    }

    for (int i=n-1;i>0;i--){
        if(arr[i]>arr[i-1])
            break;
        else if(arr[i]<arr[i-1]){
            int temp=arr[i-1];
            arr[i-1]=arr[i];
            arr[i]=temp;
        }
    }

    for(int j=0;j<n;j++){
        cout<<arr[j]<<",";
    }



}
