//
// Created by Siddhivinayak Dubey on 12/04/24.
//
#include "iostream"
using namespace std;

void permutes(string s,string combinations){
    if(s.length()==0){
        cout<<combinations<<endl;
        return;
    }
    for(int i=0 ; i<s.length(); i++){
        char currchar = s[i];
        string remaining = s.substr(0,i)+s.substr(i+1);
        permutes(remaining,combinations+currchar);
    }
}

int main(){
    permutes("abc","");
}
