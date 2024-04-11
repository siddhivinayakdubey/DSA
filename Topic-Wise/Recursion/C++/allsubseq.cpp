//
// Created by Siddhivinayak Dubey on 11/04/24.
//
#include "iostream"
using namespace std;

void allsubsequence(string s, int idx, string newString){
    if(idx == s.length()){
        cout<<newString<<endl;
        return;
    }

    char currChar = s[idx];

    /// If I want to include this character in my newString
    allsubsequence(s,idx+1,newString+currChar);

    /// If I don't want to include this caharacter in my newString
    allsubsequence(s,idx+1,newString);
}

int main(){
    allsubsequence("abc",0,"");
}