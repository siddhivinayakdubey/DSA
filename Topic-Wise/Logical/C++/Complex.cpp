//
// Created by Siddhivinayak Dubey on 02/09/21.
//

#include "iostream"
using namespace std;

class Complex{
private:
    int real;
    int img;
public:
    Complex(int r=0, int i=0){
        real=r;
        img=i;
    }
    Complex add(Complex c);
//    Complex operator+(Complex c);
    friend Complex operator+(Complex c1,Complex c2);
    void display(){
        cout<<real<<" "<<img<<endl;
    }
};

Complex operator+(Complex c1, Complex c2){
    Complex temp=0;
    temp.real=c1.real+c2.real;
    temp.img=c1.img+c2.img;
    return temp;
}


Complex Complex::add(Complex c){
    Complex temp=0;
    temp.real=c.real+real;
    temp.img=c.img+img;
    return temp;
}

//Complex Complex::operator+(Complex c){
//    Complex temp=0;
//    temp.real=c.real+real;
//    temp.img=c.img+img;
//    return temp;
//}

int main(){
    Complex c1(3,4);
    Complex c2(6,7);
    Complex c3,c4;

    c3=c1.add(c2);
    c4=c1+c2;
    c4.display();
//    cout<<c3.real<<" "<<c3.img<<endl;
//    cout<<c4.real<<" "<<c4.img;
}