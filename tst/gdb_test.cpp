/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：gdb_test.cpp
*   Author:wangle
*   CreateTime：2018-12-30
*   Description：
*
================================================================*/


#include <iostream>
using namespace std;

void swap(int &a,int &b)
{
    int tmp;
    tmp=a;
    a=b;
    b=tmp;
}

int main()
{
    int i,j;
    cout<<"input two number:"<<endl;
    cin>>i>>j;
    cout<<"before swap(),i="<<i<<"j="<<j<<endl;
    swap(i,j);
    cout<<"after swap(),i="<<i<<"j="<<j<<endl;
    // this is a reference
    return 0;

}
