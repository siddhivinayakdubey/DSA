//
// Created by Siddhivinayak Dubey on 09/09/21.
//
#include "iostream"
using namespace std;


int main(){
    int arr[]={1,2,3,4,5,6,7};
    int n=sizeof(arr)/sizeof(int);
    static int i=0,j=n-1;
    while(i<=j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
        i++;
        j--;
    }

    for (int k = 0; k < n; ++k) {
        cout<<arr[k]<<",";
    }
}

