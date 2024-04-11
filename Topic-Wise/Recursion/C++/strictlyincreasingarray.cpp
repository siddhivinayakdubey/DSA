//
// Created by Siddhivinayak Dubey on 09/04/24.
//
#include "iostream"
using namespace std;

template <size_t N>
bool strictcheck(int (&arr)[N], int i){
    size_t len = N;

    if(i==len-1){
        cout<<"strictly increasing it is"<<endl;
        return true;
    }
    if (arr[i] < arr[i+1]){
        return strictcheck(arr, i+1);
    }
    else{
        cout<<"not a strictly increasing one"<<endl;
        return false;
    }
}

int main(){
    int arr[5]={1,2,3,4,4};
    strictcheck(arr, 0);
}
