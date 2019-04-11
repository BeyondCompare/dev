# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import jieba
import jieba.analyse
import json
import hashlib 
from mylog import log
import traceback

chinese_spell_dict = {}
stop_words = set()
FULL_MODE = 1
PRECISED_MODE = 2
SEARCH_MODE = 3
FULL_SEARCH = 4
NOT_CUT = 5

def write_to_file(content,filename):
  try:
    fWriter = open(filename,'a+')
    fWriter.write(content + '\n')
  finally:
    if fWriter:
      fWriter.close()

def write_to_filepoint(content, filepoint):
  filepoint.write(content + '\n')

def read_from_file(filename):
  fReader = open(filename,'r')
  return fReader

def read_file(filename):
  fReader = open(filename,'r')
  text = ''
  try:
    text = fReader.read()
  except:
    log.error('failed to read file')
  fReader.close()
  return text

def load_stop_words(filename):
  with open(filename,'r') as fileReader:
    for word in fileReader:
      word = word.strip().replace('\n','')
      if word not in stop_words:
        stop_words.add(word)
  log.debug('stop_words size:%d'%(len(stop_words)))

def load_chinese_spell(filename):
  with open(filename,'r') as fileReader:
    for word in fileReader:
      word = word.strip().split(',')
      if word[0] and len(word) == 3:
      	if word[0] not in chinese_spell_dict:
          chinese_spell_dict[word[0]] = [word[1],word[2]]
  log.debug('size of chinese_spell_dict is:%d'%(len(chinese_spell_dict)))
        
def transfor_chinese_to_spell(word):
  spell = ''
  logogram = ''
  for i in range(len(word)):
    if word[i] in chinese_spell_dict:
      spell += chinese_spell_dict[word[i]][0]
      logogram += chinese_spell_dict[word[i]][1]
  return (spell,logogram) 

def word_segment(word,mode):
  if mode == FULL_MODE:
    word_list = jieba.lcut(word, cut_all=True)
    return word_list
  if mode == PRECISED_MODE:
    word_list = jieba.lcut(word, cut_all=False)
    return word_list
  if mode == SEARCH_MODE:
    word_list = jieba.lcut_for_search(word)
    return word_list
  if mode == FULL_SEARCH:
    search_cut = jieba.lcut_for_search(word)
    full_cut = jieba.lcut(word, cut_all=False)
    word_list = list(set(search_cut).union(set(full_cut)))
    return word_list
  if mode == NOT_CUT:
    word_list = word.split(',')
    return list(set(word_list))

def word_regulated(word):
  value = ''
  word = word.decode('utf8')
  for index in range(len(word)):
    if word[index].isdigit():
      value += word[index]
    if word[index] >= 'a' and word[index] < 'z':
      value += word[index]
    if word[index] >= u'\u4e00' and word[index]<=u'\u9fa5':
      value += word[index]
  
  return value

def calc_md5value(data):
  try:
    md5value = hashlib.md5()   
    md5value.update(data)   
    return md5value.hexdigest()
  except:
    log.error('failed to calc md5 value')
    return ''

def get_file_data(filename):
  ret = []
  try:
    f = open(filename,'r')
    for line in f.readlines():
      try:
        arr = json.loads(line)
        ret.append(tuple(arr))
      except Exception,e:
        print("%s, %s, %s" % (filename, line, e.message))
        traceback.print_exc()
  except Exception,e:
    print("%s, %s" % (filename, e.message))
    traceback.print_exc()
  finally:
    if f:
      f.close()
  return ret

if __name__ == '__main__':
  print ('begin')
  stest = ''
  print (word_regulated(stest))
  print ('end')
