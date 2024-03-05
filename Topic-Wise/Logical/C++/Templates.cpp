//
// Created by Siddhivinayak Dubey on 03/09/21.
//
#include "iostream"
using namespace std;

template<class T>
class Square{
    T x=0;
    T y=0;
public:
    T area(T x, T y);

};

template<class T>
T Square<T>::area(T x, T y){
    return x*y;
}

int main(){
    Square<int> S1;
    Square<float> S2;
    cout<<S2.area(3.5f,4.5f);
}