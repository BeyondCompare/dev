/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：cal_class_size.cpp
*   Author:wangle
*   CreateTime：2018-12-19
*   Description：
*
================================================================*/


#include <iostream>
using namespace std;
class A{};
class B:public virtual A{};
class C:public virtual A{};
class D:public B,public C{};

int main(){
cout<<"size of A:"<<sizeof(A)<<endl;
cout<<"size of b:"<<sizeof(B)<<endl;
cout<<"size of c:"<<sizeof(C)<<endl;
cout<<"size of d:"<<sizeof(D)<<endl;
return 0;
}
