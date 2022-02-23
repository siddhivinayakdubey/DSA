//
// Created by Siddhivinayak Dubey on 24/01/22.
//
#include <iostream>
using namespace std;
string LexicographicalMaxString(string str)
{
    // loop to find the max leicographic
    // substring in the substring array
    string mx = "";
    for (int i = 0; i < str.length(); ++i)
        mx = max(mx, str.substr(i));

    return mx;
}

// Driver code
int main()
{
    string str = "aabcb";
    cout << LexicographicalMaxString(str);
    return 0;
}

