//
// Created by Siddhivinayak Dubey on 09/09/21.
//

#include "iostream"
using namespace std;
///*
//
//////Left shift
//int main(){
//    int arr[]={1,2,3,4,5,6,7};
//    int n=sizeof arr/sizeof (int);
//    for(int i=1;i<n;i++){
//        arr[i-1]=arr[i];
//    }
//    arr[n-1]=0;
//
//    for (int j = 0; j <n ; ++j) {
//        cout<<"LeftShift: ";
//        cout<<arr[j]<<", ";
//    }
//}
//*/

//////Right Shift

int main(){
    int arr[]={1,2,3,4,5,6,7};
    int n=sizeof arr/sizeof (int);

    for(int i=n-1; i>0;i--){
        arr[i]=arr[i-1];
    }
    arr[0]=0;

    cout<<"Right Shift: ";
    for (int j = 0; j <n ; ++j) {

        cout<<arr[j]<<", ";
    }
}



