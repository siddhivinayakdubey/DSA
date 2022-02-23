//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include <iostream>
using namespace std;

int main(){
    int a,b,option,c;
    cout<<"Caclulator: Input two nums a & b"<<endl;
    cin>>a>>b;
    cout<<"Choose the option below";
    cout<<"1. Sum, 2. Subtract, 3.Multiply, 4.Divide";
    cin>>option;

    switch (option) {
        case 1: c=a+b;
                cout<<c;
            break;
        case 2: c=a-b;
                cout<<c;
            break;
        case 3: c=a*b;
                cout<<c;
            break;
        case 4: c=a/b;
                cout<<c;
            break;
        default:cout<<"Invalid Entry";


    }
    return 0;
}
