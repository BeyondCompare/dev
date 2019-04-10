/*================================================================
*   Copyright (C) 2019 WangLe. All rights reserved.
*   
*   FileName：anagrams.cpp
*   Author:wangle
*   CreateTime：2019-01-01
*   Description：
*
================================================================*/
//added by wangle


#include <cctype>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

void anagrams(vector<string>&strs,vector<string>&res)
{
    //vector<string>res;
    unordered_map<string,vector<string> >group;
    for(auto it:strs)
    {
        string key=it;
        sort(key.begin(),key.end());
        group[key].push_back(it);
    }//for
    for(auto it:group)
    {
        if(it->second.size()>1)
        {
            res.insert(res.begin(),it->second.begin(),it->second.end());
        }
    }
    return res;
}

int main()
{
    string a[4]={"tan","nat","abc","bca"};
    //const vector<string> strs(a);
    vector<string>strs(4,"");
    // if i want to trans strs to const vector?how to accomplish?
    for(int i=0,vector<string>::iterator it=strs.begin();it!=strs.end();++it,++i)
    {
        *it=a[i];
    }

    
    vector<string>res;
    anagrams(strs,res);
    vector<string>::iterator it=res.begin();
    for(;it!=res.end();++it)
    {
        cout<<*it<<endl;
    }
    return 0;
    
    
}
