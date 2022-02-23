//
// Created by Siddhivinayak Dubey on 09/09/21.
//
#include "iostream"
using namespace std;

//// Loop Approach
//int BinarySearch(int l , int h, int key, int arr[]){
//
//    while(l<h){
//        int m=((l+h)/2);
//        if(key==arr[m])
//            return m;
//        if(key>arr[m])
//            l=m+1;
//        if(key<arr[m])
//            h=m-1;
//
//    }
//    return -1;
//}

////Recursion

int BinarySearchRec(int l,int h, int arr[], int key){
    if(l<h){
        int m=(l+h)/2;
        if(key==arr[m])
            return m;
        else if(key<arr[m])
            return BinarySearchRec(l,m-1,arr,key);
        else if(key>arr[m]){
            return BinarySearchRec(m+1,h,arr,key);
        }
    }
}
int main(){
    int arr[]={2,5,7,9,12,14,18,19};
    cout<<BinarySearchRec(0,8,arr,18)<<endl;

    int a=5;
    int b=6;
    int sum=(a+b)/2;
    cout<<sum;


}
