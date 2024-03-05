//
// Created by Siddhivinayak Dubey on 08/09/21.
//

#include "iostream"
using namespace std;

////Normal Treeka of Recursion
//int sum(int n){
//    static int Sum=0;
//    if(n>=0){
//        Sum+=n;
//        sum(n-1);
//    }
//
//
//
//    return Sum;
//}
//// rEcurrence relation ke through
int sum(int n){
    if(n==0){
        return 0;
    }
    else{
        return sum(n-1)+n;
    }
}

int main(){
    int x= sum(5);
    cout<<x;

}