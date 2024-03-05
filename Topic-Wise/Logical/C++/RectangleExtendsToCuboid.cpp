//
// Created by Siddhivinayak Dubey on 02/09/21.
//
#include "iostream"
using namespace std;
class Rectangle{
    int length;
    int breadth;
public:
    Rectangle(int l=0 ,int b=0);
    void setLength( int l=0);
    void setBreadth(int b=0);
    int getLength();
    int getBreadth();
    int area();
    int perimeter();


};

class Cuboid:public Rectangle{
    int height;
public:
    Cuboid(int l=0,int b=0,int h=0);
    void setHeight(int h);
    int getHeight();
    int SArea();
    int Vol();


};
Cuboid::Cuboid(int l,int b,int h) {
    setLength(l);
    setBreadth(b);
    setHeight(h);
}

int Cuboid::getHeight() {
    return height;
}

int Cuboid::SArea() {
    return 2*((getLength()*getBreadth())+(getBreadth()*getHeight())+(getHeight()+getLength()));
}

int Cuboid::Vol() {
    return getLength()*getBreadth()*getHeight();
}
void Cuboid::setHeight(int h=0) {
    if(h>0){
        height=h;
    }else{
        cout<<"height cannot be negative"<<endl;
    }
}


Rectangle::Rectangle(int l,int b){
    length=l;
    breadth=b;
}

void Rectangle::setLength(int l) {
    if(l>0){
        length=l;
    }else{
        cout<<"Length cannot be negative"<<endl;
    }
}

void Rectangle::setBreadth(int b) {
    if(b>0){
        breadth=b;
    }else{
        cout<<"Breadth cannot be negative"<<endl;
    }
}

int Rectangle::getLength() {
    return length;
}

int Rectangle::getBreadth() {
    return breadth;
}

int Rectangle::area() {
    return length*breadth;
}

int Rectangle::perimeter() {
    return 2*(length+breadth);
}

int main(){
    Cuboid c(2,4);
    cout<<c.Vol()<<endl;
    cout<<c.area()<<endl;
    cout<<c.SArea();
}

