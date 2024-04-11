//
// Created by Siddhivinayak Dubey on 09/04/24.
//
#include "iostream"
using namespace std;

void reverse(string s, int idx){
    if(idx==0){
        cout<<s[idx];
        return;
    }
    cout<<s[idx];
    reverse(s, idx-1);

}

int main(){
    reverse("hello",4);
}
