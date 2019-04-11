/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：produce_consume.cpp
*   Author:wangle
*   CreateTime：2018-11-06
*   Description：
*
================================================================*/


#include <iostream>
#include <mutex>
#include <thread>
#include <condition_variable>

static const int repo_size = 10;
static const int item_total = 20;

std::mutex mtx;
std::condition_variable repo_not_full;
std::condition_variable repo_not_empty;
int item_buffer[repo_size];
static std::size_t read_pos=0;
static std::size_t write_pos=0;
std::chrono::seconds t(1);

void produce_item(int i)
{
    std::unique_lock<std::mutex> lck(mtx);
    while (((write_pos +1)%repo_size)==read_pos)
    {
        std::cout<<"producer is waiting for an empty slot";
        repo_not_full.wait(lck);
        static int
    }
}
