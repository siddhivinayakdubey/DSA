//
// Created by Siddhivinayak Dubey on 09/04/24.
//
#include "iostream"
using namespace std;
#include "deque"
#include "list"
#include "queue"
#include "stack"
#include "set"
#include "map"
#include "unordered_map"
#include "unordered_set"

int main(){

    /// ARRAYS
    cout<< "Array Functions" <<endl;

    array<int, 5> a = {1,2,3,4,5}; ///Syntax
    cout<< a.size() << " "; /// size
    cout<< a.at(2) <<" "; /// directly access the index
    //or
    cout<< a[2] <<" ";
    cout<< a.empty() <<" "; /// empty or not
    cout<< a.front() <<" "; /// first element
    cout<< a.back() <<endl; /// last element



    /// VECTORS (Dynamic Array)
    cout<< "Vector Functions" <<endl;

    vector<int> v; ///Syntax
    cout<< v.capacity()<< " "; ///dynamic sizing

    v.push_back(1); /// append at end
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);
    cout<< v.capacity()<< " "; /// Note: Capacity dynamically doubles as you enter the elements into it
    cout<< v.size() <<" "; /// size
    cout<< v.at(3) <<" "; /// directly access the index

    v.pop_back();  /// pop at end
    cout<< v.back() <<" ";

    vector<int> v1={1,2,3,4,5};
    vector<int> v2={6,7,8,9,0};

    v1.swap(v2); /// Swapping two vectors
    v1.rbegin();
    for(int nums:v1){
        cout<<  nums;
    }
    cout<<endl;


    /// DEQUE - push pop at both side
    cout<< "DEQUE IMPLEMENTATIONS"<<endl;
    deque<int> d; /// Syntax

    d.push_back(1); /// append at end
    d.push_front(2); /// append at front
    d.push_front(3);
    d.push_back(7);
    d.push_back(8);
    d.push_back(1);
    d.pop_back(); /// pop at end
    d.pop_front(); /// pop at end

    for(int nums:d){
        cout << nums;
    }

    ///LIST
    list<int> l;

    ///Code for all below

    stack<int> s;
    queue<int> q;
    priority_queue<int> pmaxi;
    priority_queue<int,vector<int>, greater<int>> pmini;
    set<int> set;


}
