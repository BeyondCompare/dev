/*================================================================
*   Copyright (C) 2018 WangLe. All rights reserved.
*   
*   FileName：produce_consume.cpp
*   Author:wangle
*   CreateTime：2018-11-18
*   Description：
*
================================================================*/


#include <unistd.h>
#include <cstdlib>
#include <condition_variable>
#include <iostream>
#include <mutex>
#include <boost/thread/thread.hpp>
#include <thread>
using namespace boost;
static const int KItemRepositorySize = 10;//item buffer
static const int KItemToProduce = 1000;//how many item need to be produced

struct ItemRepository {
    int item_buffer[KItemRepositorySize];
    size_t read_pos;
    size_t write_pos;
    std::mutex mtx;
    std::condition_variable repo_not_full;
    std:: condition_variable repo_not_empty;
}gItemRepository;

typedef struct ItemRepository ItemRepository;

void ProduceItem(ItemRepository *ir,int item)
{
    std::unique_lock<std::mutex> lock(ir->mtx);
    while(((ir->write_pos +1) % KItemRepositorySize)==ir->read_pos)
    {
        std::cout << "producer is waiting for an empty slot...\n";
        (ir->repo_not_empty).wait(lock);
    }

    (ir->item_buffer)[ir->write_pos] =item;
    (ir->write_pos)++;

    if(ir->write_pos == KItemRepositorySize)
        ir->write_pos=0;

    (ir->repo_not_empty).notify_all();
    lock.unlock();
}

int ConsumeItem(ItemRepository *ir)
{
    int data;
    std::unique_lock<std::mutex> lock(ir->mtx);
    while(ir->write_pos==ir->read_pos){
        std::cout <<"consumer is waiting for items...\n";
        (ir->repo_not_empty).wait(lock);
    }

    data =(ir->item_buffer)[ir->read_pos];
    (ir->read_pos)++;

    if(ir->read_pos >= KItemRepositorySize)
        ir->read_pos=0;
    (ir->repo_not_full).notify_all();
    lock.unlock();
    return data;
}

void ProduceTask() {
    for(int i=1;i<=KItemRepositorySize;i++)
    {
        std::cout << "produce the" <<i << "^th item..."<< std::endl;
        ProduceItem(&gItemRepository,i);
    }
}

void ConsumerTask()
{
    static int cnt =0;
    while(1){
        sleep(1);
        int item = ConsumeItem(&gItemRepository);
        std::cout << "consume the" <<item << "^th item..."<< std::endl;
        if(++cnt == KItemToProduce) break;

    }
}

void InitItemRepository(ItemRepository *ir)
{
    ir->write_pos=0;
    ir->read_pos=0;
}

int main()
{
    InitItemRepository(&gItemRepository);
    boost::thread producer(ProduceTask);
    boost::thread consumer(ConsumerTask);
    producer.join();
    consumer.join();
}















