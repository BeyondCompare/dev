/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：multi_thread_tst.cpp
*   Author:wangle
*   CreateTime：2018-12-30
*   Description：
*
================================================================*/


#include <iostream>
#include <pthread.h>
#include <unistd.h>

using namespace std;

void*td(void*ptr)
{
    for(int i=0;i<3;++i)
    {
        sleep(1);
        cout<<"this is a thread."<<endl;
    }
    return 0;
}

int main()
{
    pthread_t id;
    int ret= pthread_create(&id,NULL,td,NULL);
    if(ret)
    {
        cout<<"create thread error!"<<endl;
        return 1;
    }

    for(int i=0;i<3;++i)
    {
        cout<<"this is main process."<<endl;
        sleep(1);
    }
    pthread_join(id,NULL);
    return 0;
}
