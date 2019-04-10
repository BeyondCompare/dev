/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：test.cpp
*   Author:wangle
*   CreateTime：2018-12-29
*   Description：
*
================================================================*/


#include <iostream>
#include <string>
#include <stack>
#include <ctype.h>
#include <typeinfo>
using namespace std;


bool isNum(const char& str)
{
    if(str>='0' && str<='9')
        return true;
    else
        return false;
}

int main()
{
    //string s="3[a2[bc]]2[d]";
    string s="3[a]12[d]";
    //cout<< typeid(s).name();
    int len=s.size();
    //if(len<=1)
      //  return 1;
    string res="";
    bool left_flag=false;
    bool right_flag=false;
    int cnt=0;
    string tmpres="";
    for(int i=0;i<len;++i)
    {
        if(isNum(s[i]))
        {
            cnt=cnt*10+s[i]-'0';
            cout<<"now isNum is true,cnt is"<<cnt<<endl;
        }

        else if(s[i]=='['){
            left_flag=true;
        }
        else if(s[i]==']')
        {
            right_flag=true;
            if(left_flag && right_flag)
            {
                for(int j=0;j<cnt;++j)
                {
                    res+=tmpres;
                }
                tmpres="";
                left_flag=false;
                right_flag=false;
                cnt=0;
            }
        }
        else{
            tmpres+=s[i];//tmpres+=s.substr(i,1);
        }
    }
    cout<<res<<endl;
    return 0;

}

