#!/bin/env python
# -*-coding:utf-8-*- 

import logging
import logging.config
import sys,time

rq = time.strftime('%Y%m%d', time.localtime(time.time()))
class Log:
  def __init__(self,path):
    self.path = path 
    self.filename = self.path + 'index_building' + '.log' 
    self.logger = logging.getLogger()  

    self.fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 10) 
    self.formatter = logging.Formatter('%(asctime)s-[%(filename)s]-[line:%(lineno)d]-[%(levelname)s]: %(message)s')
    self.fh.setFormatter(self.formatter)
    self.logger.addHandler(self.fh)

    level = 4 #confHandler.getint_conf('loglevel')
    self.logger.setLevel(level)

    #self.logger.setLevel(logging.INFO)   
    #self.ch = logging.StreamHandler()    
    #gs = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s[line:%(lineno)d] - %(message)s')    
    #self.ch.setFormatter(gs)         
    #self.logger.addHandler(self.ch)
	
  def mylogger(self):
    return self.logger

  def init(self):
    logging.config.fileConfig("./conf/logging.conf")
    self.logger = logging.getLogger("root")
    return [logger, handler]

  def DEBUG(self, msg):
    self.logger.debug(msg)

  def INFO(self, msg):
    self.logger.info(msg)

  def WARN(self, msg):
    self.logger.warn(msg)

  def ERROR(self, msg):
    self.logger.error(msg)

logpath = ''
clog = Log(logpath)
log = clog.mylogger()





