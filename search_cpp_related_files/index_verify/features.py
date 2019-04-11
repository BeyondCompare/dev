#coding = 'utf8'
from util import *
from mylog import log
import os
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def handle_coreword(filename):
  core_word_index = {}
  # app_id, core_word, score
  result = get_file_data("t_app_coreword")
  if not result:
    return -1
  for item in result:
    if len(item) < 3:
      continue
    try:
      coreWord = item[1].lower()
      coreWord = word_regulated(coreWord)
      app_id = int(item[0])
      score = float(item[2])
      value = [(app_id),float(score)]
      if coreWord not in core_word_index:
        core_word_index[coreWord] = [value]
      else:
        bfind = False
        for data in core_word_index[coreWord]:
          if app_id in data:
            bfind = True
            break
        if bfind == False:
          core_word_index[coreWord].append(value)
    except:
      traceback.print_exc()

  fw = open(filename, "a+")
  if not fw:
    return 0
  for key in core_word_index:
    content = '{"' + key + '":' + str(core_word_index[key]) + '}'
    write_to_filepoint(content, fw)
  fw.close
  return 0

def handle_cluster(filename):
  cluster_info = {}
  # app_id, corr_app_id, corr_score, score
  result = get_file_data("t_app_cluster")
  if not result:
    return -1
  for item in result:
    try:
      app_id = int(item[0])
      corr_app_id = int(item[1])
      corr_score = float(item[2])
      score = float(item[3])
      value = [int(corr_app_id),float(score)]
      if int(app_id) not in cluster_info:
        cluster_info[app_id] = [value]
      else:
        cluster_info[app_id].append(value)
    except:
      traceback.print_exc()

  fw = open(filename, "a+")
  if not fw:
    return 0  
  for key in cluster_info:
    content = '{"' + str(key) + '":' + str(cluster_info[key]) + '}'
    write_to_filepoint(content, fw)
  fw.close()
  return 0

def handle_qanchor(filename):
  qanchor_info = {}
  # word, app_id, score
  result = get_file_data("t_qanchor_info")
  if not result:
    return -1
  for item in result:
    try:
      word = item[0].strip().lower()
      word  = word_regulated(word)
      app_id = int(item[1])
      score = float(item[2])
      value = [app_id, score]

      if word not in qanchor_info:
        qanchor_info[word] = [value]
      else:
        bfind = False
        for data in qanchor_info[word]:
          if app_id in data:
            bfind = True
            break
        if bfind == False:
          qanchor_info[word].append(value)
    except:
      traceback.print_exc()

  fw = open(filename, "a+")
  if not fw:
    return 0
  for key in qanchor_info:
    content = '{"' + key + '":' + str(qanchor_info[key]) + '}'
    write_to_filepoint(content, fw)
  fw.close()
  return 0

def build_features():
  if handle_coreword('result/coreword_index_data.utf8') < 0:
    return -1

  if handle_cluster('result/cluster_index_data.utf8') < 0:
    return -1

  if handle_qanchor('result/qanchor_index_data.utf8') < 0:
    return -1
 
  return 0
  
if __name__ == '__main__':
  log.debug('begin to build features...')
  #main()
  log.debug('end to build features...')
