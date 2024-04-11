//
// Created by Siddhivinayak Dubey on 09/04/24.
//

#include "iostream"
using namespace std;

int static first{-1};
int static last{-1};
void findoccurrences(string s, int idx, char c){
    if(idx==s.length()){
        cout<<first<<endl;
        cout<<last<<endl;
        return;
    }

    if(s[idx] == c){
        if(first == -1){
            first=idx;
        }
        else{
            last = idx;
        }
    }
    findoccurrences(s,idx+1,c);
}

int main(){
    findoccurrences("abcaaefaghad", 0, 'a');
}

