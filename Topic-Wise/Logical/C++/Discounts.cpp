//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include "iostream"
using namespace std;
int main(){
    float price;
    cin>>price;

    if (price<100){
        cout<<"No Discount is applicable and hence the total amount is: "<<price;
    }
    else if(price>=100 and price<500){
        //10% in this case
        price-=price*0.1;
        cout<<"The dicount is 10% for this case and hence the discounted price is: "<<price;
    }
    else if (price>=500){
        //20% in this case
        price-=price*0.2;
        cout<<"The dicount is 20% for this case and hence the discounted price is: "<<price;

    }
    return 0;
}
