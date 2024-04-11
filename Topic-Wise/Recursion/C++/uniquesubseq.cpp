//
// Created by Siddhivinayak Dubey on 11/04/24.
//
#include "iostream"
using namespace std;
#include "unordered_set"

unordered_set<string> Strings;
void uniquesubseq(string s, int idx, string newString){
    if (idx==s.length()){
        if(Strings.find(newString)==Strings.end()){
            Strings.insert(newString);
            cout<<newString<<endl;
        }
        return;
    }
    char currChar = s[idx];
    uniquesubseq(s, idx+1, newString+currChar);
    uniquesubseq(s,idx+1,newString);
}

int main(){
    uniquesubseq("aaa",0,"");
}
