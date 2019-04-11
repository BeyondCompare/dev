#coding = 'utf8'
from util import *
from index_reader import *
from index_writer import *
from appInfo import *
from features import *
import hashlib
import os,shutil
import datetime
import chardet
import json
import requests
import time
import string
import configparser
from SendVMsg import SendVMsg
from datetime import timedelta,datetime


#---- global variable -----
his_dict = {}

#---- function  -----
def load_conf(section,option):
  # load conf, the conf set the threashold val of the file_size,file_line_num and so on.
  cur_path = get_cur_path()
  conf_file = os.path.join(cur_path,"..","conf","threshold_conf")
  cp = configparser.configparser()
  cp.read(conf_file)
  return cp.get(section,option)


def get_timestamp():
  cur_time = time.strftime("%Y%m%d",time.localtime())
  return cur_time


def get_file_size(filename):
  file_path = unicode(filename,'utf8')
  fsize = os.path.getsize(file_path)
  return fsize


def chk_file_empty(filename):
  # return -1 if file is empty or not exists
  # return 0 if file is not empty
  file_path = unicode(filename,'utf8')
  if not os.path.exists(file_path):
    return -1
  if not os.path.getsize(file_path):
    return -1
  return 0


def get_file_create_time(filename):
  file_path = unicode(filename,'utf8')
  t = os.path.getctime(file_path)
  return TimeStampToTime(t)


def get_file_modify_time(filename):
  file_path = unicode(filename,'utf8')
  t = os.path.getmtime(file_path)
  return TimeStampToTime(t)


def get_file_access_time(filename):
  file_path = unicode(filename,'utf8')
  t = os.path.getatime(file_path)
  return TimeStampToTime(t)


def get_file_md5(filename):
  fobj = open(filename,'rb')
  md5_obj = hashlib.md5()
  while True:
    d = fobj.read(8096)
    if not d:
      break
    md5_obj.update(d)

  hash_code = md5_obj.hexdigest()
  fobj.close()
  md5 = str(hash_code).lower()
  return md5


def get_file_line_num(filename):
  cnt = -1
  for cnt,line in enumerate(open(filename,'rU')):
    pass
  cnt +=1
  return cnt


def get_encoding(filename):
  with open(filename,'r') as f:
    return chardet.detect(f.read())['encoding']


def alert_v_msg(msg):
  send_v_msg_instance = SendVMsg(msg)
  send_res = send_v_msg_instance.send_v_msg()
  if send_res == 0:
    return 0
  else:
    return 1


def get_file_dir(filename):
  file_path = os.path.dirname(filename)
  return file_path


def create_dir(file_path):
  if not os.path.exists(file_path):
    os.makedirs(file_path)


def get_cur_path():
  return os.getcwd()


def create_verify_res_dir():
  cur_path = get_cur_path()
  cur_time = get_timestamp()
  verify_res_dir = os.path.join(cur_path,'..','data','verify_result')  
  create_dir(verify_res_dir)
  return verify_res_dir


def create_history_today_dir(verify_res_dir):
  cur_time = get_timestamp()
  dst_dir = os.path.join(verify_res_dir,'history_verify_result',cur_time)
  create_dir(dst_dir)
  return dst_dir


def create_file(filename,file_content):
  file_path = get_file_dir(filename)
  create_dir(file_path)
  with open(filename,'a') as f:
    f.write(file_content)


def generate_history_dict(history_verify_res):
  if not os.path.exists(history_verify_res):
    return 1
  with open(history_verify_res,'r') as f:
    for line in f:
      list = line.split('\t')
      file_name = list[0]
      file_md5 = list[7]
      his_dict[file_name] = file_md5
  return 0


def get_history_date(delta):
  history_date = datetime.today() + timedelta(delta)
  history_date_format = history_date.strftime('%Y%m%d')
  return history_date_format


def get_history_verify_res(verify_res_dir,delta):
  history_date_format = get_history_date(delta)
  tmp_dir = os.path.join(verify_res_dir,'history_verify_result')
  history_data_dir = os.path.join(tmp_dir,history_date_format)
  history_verify_res = history_data_dir + '/verify_res'
  return history_verify_res 


def chk_file_updated(file_md5_val,verify_res_dir):
  '''
  return 0 if the file not updated
  return 1 if the file updated
  '''
  delta = -1
  history_verify_res = get_history_verify_res(verify_res_dir,delta)
  generate_history_dict(history_verify_res)
  if file_md5_val in his_dict:
    return 0
  else:
    return 1


def set_verify_flag(judge_res):
  flag = 2
  with open(judge_res,'r') as f:
    for line in f:
      if line.find('success') == -1:
        flag = -1
        break

  if flag == 2:
    return 0
  else:
    return -1


def create_verify_flag_file(verify_res_dir,judge_res):
  verify_flag = set_verify_flag(judge_res)
  if verify_flag == 0:
    filename = os.path.join(verify_res_dir,'verify_succ_')
  else:
    filename = os.path.join(verify_res_dir,'verify_fail_')

  file_content = " "
  cur_time = get_timestamp()
  filename = filename + cur_time
  create_file(filename,file_content)


def val_is_in_range(val,min_val,max_val):
  if val <= max_val and val >= min_val:
    return 0
  else:
    return 1


def chk_file_size_valid(file_size):
  file_size_min = load_conf('statistics_index','file_size_min')
  file_size_max = load_conf('statistics_index','file_size_max')
  if not val_is_in_range(file_size,file_size_min,file_size_max):
    return 0
  else:
    return 1


def chk_file_line_num_valid(file_line_num):
  file_line_num_min = load_conf('statistics_index','file_line_num_min')
  file_line_num_max = load_conf('statistics_index','file_line_num_max')
  if not val_is_in_range(file_line_num,file_line_num_min,file_line_num_max):
    return 0
  else:
    return 1


def generate_statistic_res(verify_res):
  file_list = load_conf('file_list','file_list')
  with open(file_list,'r') as flist:
    for filename in flist:
      empty_flag = chk_file_empty(filename)
      if empty_flag == 0:
        file_size = get_file_size(filename)
        file_line_num = get_file_line_num(filename)
        file_create_time = get_file_create_time(filename)
        file_access_time = get_file_access_time(filename)
        file_modify_time = get_file_modify_time(filename)
        file_md5_val = get_file_md5(filename)
      else:
        file_size = 0
        file_line_num = 0
        file_create_time = ''
        file_access_time = ''
        file_modify_time = ''
        file_md5_val = ''

      with open(verify_res,'a') as vrf_obj:
        res = (filename + '\t' + empty_flag + '\t' + file_size + '\t'
          + file_line_num + '\t' + file_create_time + '\t' 
          + file_access_time + '\t' + file_modify_time + '\t'
          + file_md5_val + '\n')
        vrf_obj.write(res)


def chk_verify_res(verify_res_dir,verify_res,judge_res):
  with open(verify_res,'r') as vrf_obj:
    for line in vrf_obj:
      list = line.split('\t')
      filename = list[0]
      empty_flag = list[1]
      file_size = list[2]
      file_line_num = list[3]
      file_create_time = list[4]
      file_access_time = list[5]
      file_modify_time = list[6]
      file_md5_val = list[7]
      with open(judge_res,'a') as jdr_obj:
        if empty_flag != 0:
          res = filename + 'file is empty'+'\n'
          jdr_obj.write(res)
          continue
        if chk_file_size_valid(file_size):
          res = filename + 'file_size is '+ file_size + ',not in threashold range' +'\n'
          jdr_obj.write(res)
          continue
        if chk_file_line_num_valid(file_line_num):
          res = filename + 'file_line_num is' + file_line_num + ',not in threashold range' + '\n'
          jdr_obj.write(res)
          continue
        if not chk_file_updated(file_md5_val,verify_res_dir):
          res = filename + 'file_md5_val is' + file_md5_val + ',not updated.' + '\n'
          jdr_obj.write(res)
          continue
        res = filename + 'pass all the verify.success' + '\n'
        jdr_obj.write(res)
        

def call_alert_v_msg(verify_res_dir,judge_res):
  cur_time = get_timestamp()
  succ_file = os.path.join(verify_res_dir,'verify_succ_')
  succ_file = succ_file + cur_time
  fail_file = os.path.join(verify_res_dir,'verify_fail_')
  fail_file = fail_file + cur_time
  need_call_alert = 2

  if os.path.exists(succ_file) and not os.path.exists(fail_file):
    need_call_alert = 0
  else:
    need_call_alert = 1

  if need_call_alert == 1:
    with open(judge_res,'r') as f:
      msg = ''
      for line in f:
        msg += line
      alert_v_msg(msg)
  else:
    pass
    # no need to call alert_v_msg func, verify succ


def rm_dir(dst_dir):
  if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
  else:
    pass


def clean_expired_data():
  pub_dir = load_conf('data_expire','data_expire_pub_dir')
  delta = load_conf('data_expire','data_expire_time')
  data_expire_time = get_history_date(delta)
  dst_dir = os.path.join(pub_dir,data_expire_time)
  rm_dir(dst_dir)


def get_today_files(verify_res_dir):
  if os.path.exists(verify_res_dir):
    for cur_dirs,dirs,files in os.walk(verify_res_dir):
      if files:
        return files


def backup_today_data(verify_res_dir):
  history_today_dir = create_history_today_dir(verify_res_dir)
  file_list = get_today_files(verify_res_dir)
  for line in file_list:
    src_file = os.path.join(verify_res_dir,line)
    dst_file = os.path.join(history_today_dir,line)
    shutil.copy(src_file,dst_file)


def clean_verify_res_dir(verify_res_dir):
  file_list = get_today_files(verify_res_dir)
  for line in file_list:
    complete_path = os.path.join(verify_res_dir,line)
    os.remove(complete_path)


def verify_frame():
  verify_res_dir = create_verify_res_dir()
  clean_verify_res_dir(verify_res_dir)

  verify_res = os.path.join(verify_res_dir,'verify_res')
  judge_res = os.path.join(verify_res_dir,'judge_res')

  generate_statistic_res(verify_res)
  chk_verify_res(verify_res_dir,verify_res,judge_res)
  create_verify_flag_file(verify_res_dir,judge_res)
  call_alert_v_msg(verify_res_dir,judge_res)
  clean_expired_data()
  backup_today_data(verify_res_dir)

