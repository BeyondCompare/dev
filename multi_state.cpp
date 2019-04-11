/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：multi_state.cpp
*   Author:wangle
*   CreateTime：2018-12-19
*   Description：
*
================================================================*/


#include <iostream>
using namespace std;
class CBase{
    public:
        virtual void func()
        {
            Print();
        }

        virtual void Print()
        {
            cout<<"CBase::Print"<<endl;
        }
};

class CDrieved:public CBase{
    public:
        virtual void func()
        {
            Print();
        }
        virtual void Print()
        {
            cout<<"CDrieved::Print"<<endl;
        }
};

int main()
{
    CDrieved c;
    CBase*p=&c;
    p->Print();//the output is CDRIEVED::Print
    c.func();//the output is CDRIEVED::Print
    return 0;
}

