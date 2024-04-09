//
// Created by Siddhivinayak Dubey on 09/04/24.
//

#include "iostream"
using namespace std;

int recursiveprint(int x){
    if(x != 0){
        cout<<x<<" "; //if you want to print in decreasing order
        recursiveprint(x-1);
        cout << endl;
        cout<<x<<" "; //if you want to print in increasing order
    }
}

int main(){
    recursiveprint(5);
}
