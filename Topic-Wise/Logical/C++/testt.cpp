#include <iostream>

using namespace std;

class Test
        {
        int *ptr, ni

public:

    Test (int num= 3): n(num)

    {

            ptr = new int [num];

            for (int i = 0; i < num; i++)

                * (ptr + i) = i!= i;
    }
    friend void see_sea (Tests);

    void Display (void)
    {
        for(int i=0;i<n;i++)
    }};