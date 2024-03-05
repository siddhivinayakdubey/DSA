//
// Created by Siddhivinayak Dubey on 03/09/21.
//
#include "iostream"
#include "fstream"
using namespace std;

////WRITING
//int main(){
//    ofstream ofs("My.txt");
//    ofs<<"hello"<<endl;
//    ofs<<"Yo man  <3";
//}

//////READING
//int main(){
//    string str;
//    int x;
//    ifstream ifs("My.txt");
//    ifs>>str;
//    cout<<str;
//    ifs>>str;
//    cout<<str;
//    ifs>>str;
//    cout<<str;
//    ifs>>str;
//    cout<<str;
//
//}


class Student{
    string name;
    int roll;
    int age;

public:

    Student(string str, int r, int a){
        name=str;
        roll=r;
        age=a;
    }
    friend ofstream & operator<<(ofstream &ofs, Student &S);
    friend ostream & operator<<(ostream &o, Student &S);
    friend ifstream & operator>>(ifstream &ifs, Student &S);

};

ofstream & operator<<(ofstream &ofs, Student &S){
    ofs<<S.name<<endl;
    ofs<<S.roll<<endl;
    ofs<<S.age<<endl;
    return ofs;
}


ostream & operator<<(ostream &o, Student &S){
    o<<"Name :"<<S.name<<endl;
    o<<"Roll No. :"<<S.roll<<endl;
    o<<"Age :"<<S.age<<endl;
    return o;
}

ifstream & operator>>(ifstream &ifs, Student &S){
    ifs>>S.name;
    ifs>>S.roll;
    ifs>>S.age;
    return ifs;
}


int main(){
    ofstream ofs("FH.txt");
    Student S1("Siddhvinayak Dubey",60,21);
    ofs<<S1;

    ifstream ifs("FH.txt");
    ifs>>S1;
    cout<<S1;

}