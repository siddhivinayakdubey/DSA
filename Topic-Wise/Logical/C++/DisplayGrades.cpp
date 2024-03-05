//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include <iostream>
using namespace std;

typedef int marks;

int main(){
    marks m1,m2,m3;
    float avg;
    cin>>m1>>m2>>m3;

    avg=(float)(m1+m2+m3)/3;
    cout<<"Average: "<<avg<<endl;

    if(avg>=60){
        cout<<"Grade A";
    }
    else if(avg<60 and avg>=35){
        cout<<"Grade B";
    }
    else if(avg<35){
        cout<<"Grade C";
    }
    return 0;

}
