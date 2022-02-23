//
// Created by Siddhivinayak Dubey on 08/09/21.
//

#include "iostream"
using namespace std;

//// APPROACH-1
//int TS(int x, int n){
//    static int p=1,f=1;
//    int r;
//
//    if(n==0)
//        return 1;
//    else
//        TS(x,n-1);
//        p=p*x;
//        f=f*n;
//        r=r+p/f;
//    return r;
//}


//// APPROACH 2- Horners rule of sbko common le lene ka

//int TS(int x, int n){
//    int r=1;
//    if(n==0)
//        return 1;
//    else
//        while(n>0){
//            r=(r*(x/n))+1;
//            n--;
//        }
//    return r;
//}


int TS(int x, int n){
    static int r =1;

    if (n==0)
        return 1;
    else
        r=(r*(x/n))+1;
        TS(x,n-1);
    return r;

}
////APPROACH 3- Horners ka recursion
int main(){
    cout<<TS(2,2);
}