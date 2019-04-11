#coding = 'utf8'
from util import *

class CAppField:
  def __init__(self,appid = 0,name = ' ',download = 0,grade = 0,quality = 0.0,tags = ' ',category = ''):
    self._appid = appid
    self._name = name
    self._download = download
    self._quality = quality
    self._tags = tags
    self._category = category
    self._grade = grade

  @property
  def appid(self):
    return self._appid
  
  @appid.setter
  def appid(self,val):
    self._appid = val

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self,val):
    self._name = val

  @property
  def download(self):
    return self._download

  @download.setter
  def download(self,val):
    self._download = val

  @property
  def quality(self):
    return self._quality

  @quality.setter
  def quality(self,val):
    self._quality = val

  @property
  def tags(self):
    return self._tags

  @tags.setter
  def tags(self,val):
    self._tags = val

  @property
  def category(self):
    return self._category

  @category.setter
  def category(self,val):
    self._category = val

  @property
  def grade(self):
    return self._grade

  @grade.setter
  def grade(self,val):
    self._grade = val

  def __str__(self):
    return 'appid={0}##category={1}'.format(self._appid,self._category)

class CAppInfo:
  def __init__(self):
    self.app_info_dict = {}

  def __iter__(self):
    for key in self.app_info_dict:
      yield self.app_info_dict[key]

  def get_app_info(self):
    # appid, app_cn_name, real_downloadCount, app_type, app_icon, app_apk, grade
    result = get_file_data("t_app_info") 
    if not result:
      return -1
    for item in result:
      if not item[1] or item[1] is None:
        continue

      if not item[4] or item[4] is None:
        continue

      if not item[5] or item[5] is None:
        continue

      try:
        appid = int(item[0])
        appName = item[1].strip()
        download = int(item[2])
        grade = int(item[6])
        field = CAppField(appid,appName,download,grade)
        if appid not in self.app_info_dict:
          self.app_info_dict[appid] = field        
      except:
        traceback.print_exc()
    return 0

  def get_app_download(self):
    # app_id, download_count
    result = get_file_data("t_app_download")
    if not result:
      return -1
    for item in result:
      try:
        appid = int(item[0])
        download = int(item[1])
        if download == 0:
          continue
        if appid in self.app_info_dict:
          self.app_info_dict[appid].download = download
      except:
        traceback.print_exc()
    return 0

  def combine_app_info(self):
    if self.get_app_info() == 0:
      if self.get_app_download() == 0:
        return 0
    return -1
    #self.get_app_quality()

  def get_appinfo_size(self):
    return len(self.app_info_dict)

if __name__ == '__main__':
  print ('begin')
  print ('end')
