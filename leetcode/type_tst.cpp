/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：type_tst.cpp
*   Author:wangle
*   CreateTime：2018-12-29
*   Description：
*
================================================================*/


#include <iostream>
#include <ctype.h>
#include <typeinfo>
using namespace std;
int main()
{
    char chr='9';
    string str="ggg";
    int num=1;
    class aggd{};
    class B:public aggd{};
    class C:public B{};
    B b;
    aggd& ab=b;
    cout << typeid(ab).name()<<endl;
    C smc;
    B& smb=smc;
    cout << typeid(smb).name()<<endl;
    cout << typeid(smc).name()<<endl;
    //cout<<typeid(abc)<<typeid(str)<<typeid(num)<<endl;
    return 0;
}
