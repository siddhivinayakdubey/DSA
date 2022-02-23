#include <iostream>
using namespace std;

void insertionsort(int arr[], int n);
void printthird(int arr[], int size);

int main() {
    int arr[5]={17,14,31,13,2};
    insertionsort(arr);
    return 0;
}

void insertionsort(int arr[]){
    int i,j,key;

    for(i=1;i<=n;i++){
        key=arr[i];
        j=i-1;
        while(j>=0 && key<arr[j]){
            arr[j+1]=arr[j];
            j--;
        arr[j+1]=key;
        }
    }
}

void printthird(int arr[], int size){
    int x;
    x=arr[n-2];
    cout<<x;
    cout<<endl;
}
