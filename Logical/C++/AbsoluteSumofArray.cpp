//
// Created by Siddhivinayak Dubey on 27/08/21.
//

#include "iostream"
using namespace std;

int main(){
    int nums[]={2,3,5};
    int sum=0;
    int n=sizeof(nums)/sizeof(nums[0]);

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
           int value=abs(nums[i]-nums[j]);
           sum+=value;
           cout<<sum<<endl;
        }
    }

}