//
// Created by Siddhivinayak Dubey on 03/09/21.
//
#include "iostream"
using namespace std;

template<class T>
class Rectangle{
    int length=0;
    int breadth=0;

public:
    T area(T length, T breadth);
    T perimeter(T length, T breadth);
};

template<class T>
T Rectangle<T>::area(T length, T breadth){
    return length*breadth;
}

template<class T>
T Rectangle<T>::perimeter(T length, T breadth) {
    return 2*(length+breadth);
}


int main(){
    Rectangle<int> r1;
    Rectangle<float> r2;

    cout<<r1.perimeter(3,4)<<endl;
    cout<<r2.area(5.78645,7.346977);

}