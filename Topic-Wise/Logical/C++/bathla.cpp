#include <math.h>
#include <time.h>
#include <ctype.h>
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <array>
#include <sstream>
#include <regex>
using namespace std;

char change_case(char c)
{
    if (isupper(c))
        return tolower(c);
    else
        return toupper(c);
}

int sumOfDigits(int n)
{
    int sum = 0;
    while (n > 0)
    {
        sum += n % 10;
        n = n / 10;
    }
    return sum;
}

float multiplyBy2(float f)
{
    float ans = 0;
    ans = f * 2;
    return ans;
}

string SwitchBoolean(bool val)
{
    if (val)
    {
        return "true = false";
    }
    else
    {
        return "false = true";
    }
}
bool isNumber(const string &str)
{
    for (char const &c : str)
    {
        if (isdigit(c) == 0)
            return false;
    }
    return true;
}
bool isFloat(const string &str)
{
    static const regex doubleRegex{R"([+-]?([0-9]*[.])?[0-9]+)"};
    if (regex_match(str, doubleRegex)){
        return true;
    }
    return false;
}
string solve(string str)
{
    // code goes here...s
    if (isNumber(str))
    {
        stringstream geek(str);
        int x = 0;
        geek >> x;
        str = str + "=" + to_string(sumOfDigits(x));
    }
    else if(isFloat(str)){
        stringstream geek(str);
        int x = 0;
        geek >> x;
        str = str + "=" + to_string(multiplyBy2(x));
    }
    return str;
}
int main()
{

    string str = "This is a 999 sampLE 123.45 inPut for the true assignMENT";

    string word = "";
    string ans = "";
    for (auto x : str)
    {
        if (x == ' ')
        {
            // cout << word << endl;
            ans = ans + solve(word);
            word = "";
        }
        else
        {
            word = word + x;
        }
    }
    // cout << word << endl;
    solve(word);
    cout << ans;
    return 0;
}