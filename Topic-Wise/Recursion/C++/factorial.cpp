//
// Created by Siddhivinayak Dubey on 09/04/24.
//

#include "iostream"
using namespace std;

int factorial(int x){
    if(x==1 || x==0) return 1;
    int fact_nm1 = factorial(x-1);
    int fact = x * fact_nm1;
    return fact;

}

int main(){
    cout<<factorial(5);
}