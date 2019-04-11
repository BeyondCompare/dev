#coding = 'utf8'
from mylog import log
from similarity import bm25Similarity,QueryDocInfo
from util import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class CIndexWriter:
  def __init__(self,fieldObj):
    self.fieldObj = fieldObj
    self.total_word = 0
    self.reversed_index = {}
    self.field_word_counts = {}

  def build_posting_list(self,fieldValue,appid,mode):
    fieldValue = fieldValue.lower()
    word_list = word_segment(fieldValue,mode)
    word_count = 0
    for word in word_list:
      if len(word) == 0 or word in stop_words:
        continue
      word_count = word_count + 1
      word = word.strip()
      if word not in self.reversed_index:
        self.reversed_index[word] = [[appid,fieldValue.count(word) + 1]]
      else:
        self.reversed_index[word].append([appid,fieldValue.count(word) + 1])
    
    return word_count

  def build_index(self,mode = FULL_MODE,filename = ''):
    log.debug('begin to build reversed index')
    self.total_word = 0
    self.field_word_counts.clear()
    self.reversed_index.clear()
    for field in self.fieldObj:
      appid = field.appid
      fieldValue = field.name
      word_count = 0
      word_count += self.build_posting_list(fieldValue,appid,mode)
      if appid not in self.field_word_counts:
      	self.field_word_counts[appid] = word_count
      self.total_word += word_count 

  def build_index_save(self,mode = FULL_MODE,filename = ''):
    log.debug('begin to build reversed index')
    self.total_word = 0
    self.field_word_counts.clear()
    self.reversed_index.clear()
    if not filename:
      return
    fw = open(filename, "a+")
    if not fw:
      return
    for field in self.fieldObj:
      appid = field.appid
      fieldValue = field.name
      
      word_count = 0
      word_count += self.build_posting_list(fieldValue,appid,mode)

      if appid not in self.field_word_counts:
      	self.field_word_counts[appid] = word_count

      fieldValue = fieldValue.replace('"',"'").replace('-','')
      if hasattr(field,'download'):
        content = '[' + str(appid) + ',"' + fieldValue + '",' + str(field.download) + ',' + str(field.grade) + ',' + str(word_count)  + ']'
      else:
        content = '[' + str(appid) + ',"' + fieldValue + '"' + ']'
      write_to_filepoint(content, fw)
      
      self.total_word += word_count
    fw.close()

  def score(self,filename,docCounts,bmaxscore = False,maxscore_filename = ''):
    nDocCount = docCounts
    nAvgTerms = self.total_word / nDocCount
    log.debug('DocCount = %d,total_word = %d'%(nDocCount,self.total_word))

    index_data = {}
    maxscore_dict = {}
    for word in self.reversed_index:
      nDocFreq = len(self.reversed_index[word])
      maxscore = 0.0
      for item in self.reversed_index[word]:
        appid = item[0]
        nDocTerms = self.field_word_counts[appid]
        nFreq = item[1]
        queryDocInfo = QueryDocInfo(nDocFreq=nDocFreq,nDocCount=nDocCount,nDocTerms=nDocTerms,nFreq=nFreq,nAvgTerms=nAvgTerms)
        score = bm25Similarity.getSimilarity(queryDocInfo)
        if score > maxscore:
          maxscore = score
        if word not in index_data:
          index_data[word] = [[appid,score]]
        else:
          index_data[word].append([appid,score])

      if word not in maxscore_dict:
        maxscore_dict[word] = maxscore
    
    fw = open(filename, "a+")
    if not fw:
      return
    for word in index_data:
      maxscore = maxscore_dict[word]
      item = index_data[word]
      data = [[value[0],value[1] / maxscore] for value in item]
      content = '{"' + word + '":' + str(data) + '}'
      write_to_filepoint(content,fw)

      spell_logogram = transfor_chinese_to_spell(word)
      if spell_logogram[0]:
        word_spell = spell_logogram[0]
        content = '{"' + word_spell + '":' + str(data) + '}'
        write_to_filepoint(content,fw)
        
      if spell_logogram[1]:
        word_logogram = spell_logogram[1]
        content = '{"' + word_logogram + '":' + str(data) + '}'
        write_to_filepoint(content,fw)
    fw.close()
    if bmaxscore:
      for word in maxscore_dict:
        content = '["' + word + '",' + str(maxscore_dict[word]) + ']'
        write_to_file(content,maxscore_filename)


      
