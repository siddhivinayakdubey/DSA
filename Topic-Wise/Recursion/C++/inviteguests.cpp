//
// Created by Siddhivinayak Dubey on 12/04/24.
//

#include "iostream"
using namespace std;

int inviteguests(int n){

    if(n<=1){
        return 1;
    }

    //invite single guests
    int single = inviteguests(n-1);

    //invite guests in pairs
    int pairs = (n-1) * inviteguests(n-2);

    return single + pairs;
}

int main(){
    int yayy = inviteguests(4);
    cout<<yayy;
    return 0;
}

