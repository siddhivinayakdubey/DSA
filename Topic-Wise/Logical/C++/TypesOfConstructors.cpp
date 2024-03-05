//
// Created by Siddhivinayak Dubey on 01/09/21.
//

#include "iostream"
using namespace std;

class Rectangle{
    int length;
    int breadth;

public:
    int setLength(int l){
        if(l>=0){
            length=l;
        }else{
            cout<<"Length cannot be negative"<<endl;
            length=0;
        }
    }

    int setBreadth(int b){
        if(b>=0){
            breadth=b;
        }else{
            cout<<"Breadth cannot be negative"<<endl;
            breadth=0;
        }
    }

    int getLength(){
        return length;
    }

    int getBreadth(){
        return breadth;
    }

    int area(){
        return length*breadth;
    }

    int perimeter(){
        return 2*(length+breadth);
    }

    ////CONSTRUCTORS:

    ////DEFAULT or NON-PARAMETERISED
//    Rectangle(){
//        length=0;
//        breadth=0;
//    }

    ////PARAMETERIZED
//    Rectangle(int l,int b){
//        setLength(l);
//        setBreadth(b);
//    }

    ////COPY CONSTRUCTOR
    Rectangle(Rectangle  &r){
        length=r.length;
        breadth=r.breadth;
    }

    //// COMBINING PARAMETERISED+NONPARAMETERISED

    Rectangle(int l=0,int b=0){
        setLength(l);
        setBreadth(b);
    }

};

int main(){
    Rectangle r1;
    Rectangle r2(5,10);
    Rectangle r3(5);
    Rectangle r4(r2);

    cout<<r1.area()<<" "<<r2.area()<<" "<<r3.area()<<" "<<r4.area()<<endl;
    cout<<r1.perimeter()<<" "<<r2.perimeter()<<" "<<r3.perimeter()<<" "<<r4.perimeter();
}