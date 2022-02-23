//
// Created by Siddhivinayak Dubey on 13/09/21.
//

#include "iostream"
using namespace std;

class LowerTriangle{
    int n;
    int *A;

public:
    LowerTriangle(int n){
        this->n=n;
        A=new int [n*(n+1)/2];
    }

    void set(int i, int j, int x){
        if(j<=i){
            A[(i*(i-1)/2)+j-1]=x;
        }
    }

    int get(int i, int j){
        if(j<=i){
            return A[(i*(i-1)/2)+j-1];
        }
        else{
            return 0;
        }
    }


    void Display(){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(j<=i){
                    cout<<A[(i*(i-1)/2)+j-1]<<" ";
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

    LowerTriangle d(3);
    d.set(1,2,5);
    d.set(3,2,6);
    d.set(1,2,4);
    d.set(3,3,9);
    d.Display();
}
