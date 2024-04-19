//
// Created by Siddhivinayak Dubey on 12/04/24.
//

#include "iostream"
using namespace std;
#include "vector"

void mazepaths(int i,int j,int m, int n,string path){
    if(i==m-1 and j==n-1){
        cout<<path<<endl;
        return;
    }

    if (i<m-1){
        mazepaths(i+1,j,m,n,path+'R');
    }
    if (j<n-1){
        mazepaths(i,j+1,m,n,path+'D');
    }
}

int main(){
    mazepaths(0,0,3,3,"");
}