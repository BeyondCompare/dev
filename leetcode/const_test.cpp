/*================================================================
*   Copyright (C) 2019 WangLe. All rights reserved.
*   
*   FileName：const_test.cpp
*   Author:wangle
*   CreateTime：2019-01-01
*   Description：
*
================================================================*/


#include <vector>
#include <iostream>
#include <string>
using namespace std;

void prt(const vector<string>&strs)
{
    cout<<strs.size()<<endl;
}

int main()
{
    string a[3]={"abc","nat","tan"};
    vector<string>strs(a,a+3);
    prt(strs);
    return 0;
}
