//
// Created by Siddhivinayak Dubey on 01/09/21.
//
#include "iostream"
using namespace std;

class Rectangle{
public:
    int length;
    int breadth;

    int area(){
        return length*breadth;
    }

    int perimeter(){
        return 2*(length+breadth);
    }
};

int main(){
    Rectangle r1,r2;
    Rectangle *p;
    p=&r2;
    Rectangle *q=new Rectangle();
    r1.length=10;
    r1.breadth=15;
    cout<<r1.area()<<endl;
    cout<<r1.perimeter()<<endl;

    p->length=60;
    p->breadth=30;
    cout<<r2.area()<<endl;
    cout<<p->area()<<endl;
    cout<<r2.perimeter()<<endl;

    q->breadth=70;
    q->length=65;
    cout<<q->area();
}
