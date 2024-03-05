#include<iostream>
using namespace std;
int joshibkl(int arr[],int ds){
    int max_diff=INT_MAX;
    int sum=0;

    for(int i=0;i<sizeof(arr)/sizeof(int);i++){
        for(int j=i+1;j<sizeof(arr)/sizeof(int);j++){
            int diff=arr[i]-arr[j];
            if(abs(abs(diff)-ds)<max_diff){
                max_diff=diff;
                sum=arr[i]+arr[j];
            }
        }
    }

    return sum;

}

int main(){
    int ds=5;
    int arr[]={2,1,4,2,3,2,2,6};
    cout<<joshibkl(arr,ds);
}