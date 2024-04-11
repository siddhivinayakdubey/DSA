//
// Created by Siddhivinayak Dubey on 11/04/24.
//
#include "iostream"
using namespace std;

string newString{};
void MoveX(string s, int idx, int count){
    if(idx == s.length()){
        newString.append(count, 'x');
        cout<<newString;
        return;
    }
    if(s[idx] != 'x'){
        newString +=s[idx];
    }
    else{
        count+=1;
    }
    MoveX(s, idx+1, count);
}

int main(){
    MoveX("ababdcxxbdbsxbsbsbx",0, 0);

}

