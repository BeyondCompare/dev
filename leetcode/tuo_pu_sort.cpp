/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：tuo_pu_sort.cpp
*   Author:wangle
*   CreateTime：2018-12-21
*   Description：
*
================================================================*/


#include <iostream>
#include <list>
#include <queue>
using namespace std;

class Graph{
    int V;
    queue<int> q;
    int* indegree;
public:
    Graph(int V);
    ~Graph();
    void addEdge(int v,int w);
    bool topological_sort();
};

Graph::Graph(int V)
{
    this->V=V;
    adj =new list<int>[V];

    indegree =new int[V];
    for(int i=0;i<V;++i)
    {
        indegree[i]=0;
    }
}

Graph::~Graph()
{
    delete []adj;
    delete []indegree;
}

void Graph::addEdge(int v,int w)
{
    adj[V].push_back(w);
    ++indegree[w];
}

bool Graph::topological_sort()
{
    for(int i=0;i<V;++i)
    {
        if(indegree[i]==0)
            q.push(i);
    }

    int cnt=0;
    while(!q.empty())
    {
        int v=q.front();
        q.pop();

        cout<< v <<" ";
        ++cnt;

        list<int>::iterator beg=adj[v].begin();
        for(;beg!=adj[v].end();++beg)
        {
            if(!(--indegree[*beg]))
                q.push(*beg);
        }
    }//while
    if(cnt<V)
        return false;
    else
        return true;
}
