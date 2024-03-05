//
// Created by Siddhivinayak Dubey on 13/09/21.
//

#include "iostream"
using namespace std;

class Diagonal{
    int n;
    int *A;

public:
    Diagonal(int n){
        this->n=n;
        A=new int [n];
    }

    void set(int i, int j, int x){
        if(i==j){
            A[i-1]=x;
        }
    }

    int get(int i, int j){
        if(i==j){
            return A[i-1];
        }
        else{
            return 0;
        }
    }


    void Display(){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(i==j){
                    cout<<A[i-1]<<" ";
                }
                else{
                    cout<<"0"<<" ";
                }
            }
            cout<<endl;
        }
    }
};

int main(){

    Diagonal d(3);
    d.set(1,1,5);
    d.set(2,2,6);
    d.set(3,3,9);
    d.Display();
}