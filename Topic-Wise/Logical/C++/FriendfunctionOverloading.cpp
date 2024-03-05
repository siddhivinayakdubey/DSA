//
// Created by Siddhivinayak Dubey on 02/09/21.
//
#include "iostream"
using namespace std;

class Complex{
    int real;
    int img;

public:
    Complex(int r=0,int i=0){
        real=r;
        img=i;
    }
    friend Complex operator+(Complex c1, Complex c2);
    friend ostream & operator<<(ostream &o,Complex c);
};


Complex operator+(Complex c1,Complex c2){
    Complex temp;
    temp.real=c1.real+c2.real;
    temp.img=c1.img+c2.img;

    return temp;
}

ostream & operator<<(ostream &o,Complex c){
    o<<c.real<<"+i"<<c.img;
    return o;
}


int main(){
    Complex c1(3,4);
    Complex c2(5,7);
    Complex c3;
    c3=c1+c2;
    cout<<c3;
}