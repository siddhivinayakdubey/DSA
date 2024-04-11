//
// Created by Siddhivinayak Dubey on 12/04/24.
//

#include "iostream"
using namespace std;

unordered_map<int,string> keypad = {
        {0,"."},
        {1,"abc"},
        {2,"def"},
        {3,"ghi"},
        {4,"jkl"},
        {5,"mno"},
        {6,"pqrs"},
        {7,"tuv"},
        {8,"wxyz"}
};

void printcomb(string s, int idx, string combinations){
    if(idx==s.length()){
        cout<<combinations<<endl;
        return;
    }

    int currint = s[idx]-'0';
    string mappings = keypad[currint];

    for(int i=0 ; i<mappings.length() ; i++){
        printcomb(s,idx+1,combinations+mappings[i]);
    }
}

int main(){
    printcomb("23",0,"");
}
