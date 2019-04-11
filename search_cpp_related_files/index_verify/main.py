#coding = 'utf8'
from util import *
from index_reader import *
from index_writer import *
from appInfo import *
from features import *
import os,shutil

def keyword_index(filename):
  keywordObj = CIndexReader()
  if keywordObj.get_field_info("t_aso_app_message") < 0:
    return -1
  docCounts = keywordObj.get_field_size()

  indexWriter  = CIndexWriter(keywordObj)
  indexWriter.build_index()
  indexWriter.score(filename,docCounts)
  return 0

def appointmentgame_index(filename):
  gameObj = CIndexReader()
  if gameObj.get_field_info("t_appointment_game") < 0:
    return -1
  docCounts = gameObj.get_field_size()

  indexWriter  = CIndexWriter(gameObj)
  indexWriter.build_index_save(filename = 'result/appointment_game_info.utf8')
  indexWriter.score(filename,docCounts)
  return 0

def text_index(filename):
  appinfoObj = CAppInfo()
  if appinfoObj.combine_app_info() < 0:
    return -1
  docCounts = appinfoObj.get_appinfo_size()

  indexWriter  = CIndexWriter(appinfoObj)
  indexWriter.build_index_save(filename='result/app_info.utf8')
  indexWriter.score(filename,docCounts,bmaxscore = True,maxscore_filename = 'result/max_score_info.utf8')
  return 0

def remove_file():
  if not os.path.exists("result"): 
    os.makedirs("result")
  for filename in os.listdir('result'):
    if os.path.exists('result/' + filename):
      os.remove('result/'+ filename)

def verify_frame(result_path):
  if not os.path.exists(result_path):
    return -1
  # start general verify subprocess
  for item in os.listdir(result_path):
    filename=result_path+'/'+item
    if chk_empty(filename)<0:
      remove_file()
      return
    if 
      # chk_empty
      # chk_fileline
      # chk_file_size
      # chk_file_format(this is unique)
      # 是否如果一个文件为空，则这批数据都不能推送到线上生效？如果是，则检测结果为空便直接return -1即可。
      # 

def main():
  remove_file()
  load_chinese_spell('etc/spell.utf8')
  load_stop_words('etc/stop_words.utf8')
  if build_features() < 0:
    remove_file()
    return
  if keyword_index('result/keyword_index_data.utf8') < 0:
    remove_file()
    return
  if appointmentgame_index('result/appointment_game_index_data.utf8') < 0:
    remove_file()
    return
  if text_index('result/text_index_data.utf8') < 0:
    remove_file()
    return
    ###
    # added by wangle @ 2019-3-21 20:00:16,数据校验函数放在这里
    # 获取/result目录下的所有非md5文件，其实就是keyword_index_data.utf8
    # appointment_game_index_data.utf8和text_index_data.utf8
    # 然后对这三个文件进行统计信息校验，历史版本校验，以及预留一个接口，进行策略校验
    ### 写一个frame函数，传入result的路径，然后内部调用各种校验函数即可。
  
  for item in os.listdir('result') :
    filename = 'result/' + item
    if os.path.exists(filename):
      data = read_file(filename)
      md5value = calc_md5value(data)
      if md5value:
        md5filename = 'result/' + 'md5_' + item
        with open(md5filename,'w') as fileobject:
          fileobject.write(md5value)

if __name__ == '__main__':
  print ('begin buinding index...')
  main()
  print ('end building index')
