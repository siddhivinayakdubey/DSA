//
// Created by Siddhivinayak Dubey on 11/04/24.
//
#include "iostream"
using namespace std;
#include "unordered_set"

unordered_set<char> Chars;

void removeduplicates(string s, int idx){
    if(idx == s.length()){
        cout<<s;
        return;
    }
    if(Chars.find(s[idx]) == Chars.end()){
        Chars.insert(s[idx]);
    }
    else{
        s.erase(idx,1);
        idx-=1;
    }
    removeduplicates(s, idx+1);
}

int main(){
    removeduplicates("abbcdddebdceba", 0);
}
