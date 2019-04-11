/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：test.cpp
*   Author:wangle
*   CreateTime：2018-11-19
*   Description：
*
================================================================*/


#include <iostream>
#include <cstring>
#include <cctype>
#include <stack>
using namespace std;

int foo()
{
    int curlen,maxlen=0;
    cout<< curlen<<endl;
    cout<< maxlen<<endl;
    return 0;
}


int main(){
    stack<int>stk;
    for(int i=0;i<10000;++i)
    {
        stk.push(i);
    }
    cout << stk.size()<<endl;

}
