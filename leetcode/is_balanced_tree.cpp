/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：is_balanced_tree.cpp
*   Author:wangle
*   CreateTime：2018-12-20
*   Description：
*
================================================================*/


#include <iostream>
using namespace std;

struct btn{
int val;
btn*left;
btn*right;
};

bool IsBalancedSpec(btn*root,int*depth)
{
    if(!root)
    {
        *depth=0;
        return true;
    }
    //judge the left and right sub-tree is balanced;
    int left,right=0;
    bool left_flag,right_flag;
    left_flag=IsBalancedSpec(root->left,&left);
    right_flag=IsBalancedSpec(root->right,&right);
    if(left_flag && right_flag)
    {
        int diff=left-right;
        if(diff>=-1 && diff<=1)
        {
            *depth=1+(left>right?left:right);
            return true;
        }
    }
    return false;
}

bool IsBalanced(btn*root)
{
    int depth=0;
    return IsBalancedSpec(root,&depth);
}

void GetMirror(btn*root)
{
    // 前序遍历，交换左右节点
    // 直到叶子结点
    if(!root)
        return;
    if(!root->left && !root->right)
        return;
    btn*tmp=root->left;
    root->left=root->right;
    root->right=tmp;
    // if not leaf node, call this func recursively
    if(root->left)
        GetMirror(root->left);
    if(root->right)
        GetMirror(root->right);
}

// judge two binary tree is mirror or not
// 同一棵树，不过r1 r2都是同一个根节点root。
bool IsMirror(btn*r1,btn*r2){
    if(!r1 && !r2)
        return true;
    if(!r1|| !r2)
        return false;
    if(r1->val!=r2->val)
        return false;
    bool left_flag,right_flag;
    left_flag=IsMirror(r1->left,r2->right);
    right_flag=IsMirror(r1->right,r2->left);
    return left_flag && right_flag;
}



//层序遍历二叉树


