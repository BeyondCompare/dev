/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：mtx_tst.cpp
*   Author:wangle
*   CreateTime：2018-11-18
*   Description：
*
================================================================*/


#include <boost/thread/thread.hpp>
#include <boost/thread/mutex.hpp>
#include <boost/bind.hpp>
#include <iostream>

using namespace std;
boost::mutex io_mtx;

void count(int id)
{
    for(int i=0;i<10;i++)
    {
        boost::mutex::scoped_lock lock(io_mtx);
        std::cout<<id<<":"<< i<<std::endl;
    }
}


int main()
{
    boost::thread t1(boost::bind(&count,1));
    boost::thread t2(boost::bind(&count,2));
    t1.join();
    t2.join();
    return 0;
}
