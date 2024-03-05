//
// Created by Siddhivinayak Dubey on 27/08/21.
//

#include "iostream"
using namespace std;

//int main(){
//    //PATTERN-1:
//    //1 2 3 4
//    //5 6 7 8
//    //9 10 11 12
//    //13 14 15 16
//
//    int count=1;
//    for(int i=0;i<4;i++){
//        for(int j=0;j<4;j++){
//            cout<<count<<" ";
//            count+=1;
//        }
//        cout<<endl;
//    }
//
//}

//int main(){
//    //PATTERM-2
////    *
////    **
////    ***
////    ****
//    char star='*';
//    for(int i=0;i<4;i++){
//        for(int j=0;j<=i;j++){
//            cout<<star;
//        }
//        cout<<endl;
//    }
//
//}
//int main(){
//    //PATTERM-2
//    //       *
//    //      **
//    //     ***
//    //    ****
//    char star='*';
//    for(int i=0;i<4;i++){
//        for(int j=0;j<4;j++){
//            if(i+j>=3){
//                cout<<star;
//            }
//            else{
//                cout<<" ";
//            }
//
//        }
//        cout<<endl;
//    }
//
//}

int main(){
    //PATTERM-2
    //       *
    //      **
    //     ***
    //    ****
    char star='*';
    for(int i=0;i<4;i++){
        for(int j=4;j>=0;j--){

                cout<<"_";
        }
        cout<<endl;
    }

}