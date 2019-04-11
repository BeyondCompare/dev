/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：find_target_sum_in_binary_tree.cpp
*   Author:wangle
*   CreateTime：2018-12-20
*   Description：
*
================================================================*/


#include <iostream>
#include <vector>
using namespace std;

struct btn{
int val;
btn*left;
btn*right;
};

void FindPath(int target_num,btn*root)
{
    if(!root)
        return;
    vector<int>path;
    int cur_sum=0;
    FindPathSpec(target_num,root,path,cur_sum);

}
void FindPathSpec(int target_num,btn*root,vector<int>&path,int cur_sum)
{
    cur_sum+=root->val;
    path.push_back(root->val);
    bool isleaf=false;
    if(!root->left && !root->right)
        isleaf=true;
    if(cur_sum==target_num && isleaf)
    {
    // finish find the path,output it;
        cout<<"the path is found\n";
        vector<int>::iterator it=path.begin();
        for(;it!=path.end();++it)
        {
            cout<<*it<<"\t";
        }
    }
    if(root->left)
        FindPathSpec(target_num,root->left,path,cur_sum);
    if(root->right)
        FindPathSpec(target_num,root->left,path,cur_sum);
    path.pop_back();
}
