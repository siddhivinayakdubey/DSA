//
// Created by Siddhivinayak Dubey on 09/04/24.
//

#include "iostream"
using namespace std;

////with stack height n
//int power(int x, int n){
//    if(n==0){
//        return 1;
//    }
//    if (x==0){
//        return 0;
//    }
//
//    int p_mn1 = power(x,n-1);
//    int p = x * p_mn1;
//
//    return p;
//}

////with stack height logn
int power(int x, int n){
    if (n==0){
        return 1;
    }
    if (x==0){
        return 0;
    }

    int p_by2= power(x,n/2);

    if (n%2==0){
        return p_by2 * p_by2;
    }
    else{
        return p_by2 * p_by2 * x;
    }
}

int main(){
    cout<<power(5,3);
}