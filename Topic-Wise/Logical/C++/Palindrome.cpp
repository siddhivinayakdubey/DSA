//
// Created by Siddhivinayak Dubey on 27/08/21.
//
#include "iostream"
using namespace std;

int main(){
     int n,r,temp,rev=0;
     cin>>n;
     temp=n;

     while(n>0){
         r=n%10;
         rev=rev*10+r;
         n=n/10;
     }

     if((int)rev==temp){
         cout<<"Palindrome hai";

     }
     else{
         cout<<"Palindrone nahi hai";
     }
}