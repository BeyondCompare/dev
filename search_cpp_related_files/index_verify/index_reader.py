#coding = 'utf8'
from util import *

class CField:
  def __init__(self,appid = 0,name = ' '):
    self._appid = appid
    self._name = name

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


class CIndexReader:
  def __init__(self):
    self.field_info_dict = {}

  def __iter__(self):
    for key in self.field_info_dict:
      yield self.field_info_dict[key]

  def get_field_info(self, filename):
    # appid, app_cn_name
    result = get_file_data(filename)
    if not result:
      return -1
    for item in result:
      try:
        appid = int(item[0])
        name = item[1]
        if not name or name is None:
          continue
        name = name.strip().lower()
        field = CField(appid,name)
        if appid not in self.field_info_dict:
          self.field_info_dict[appid] = field
      except:
        traceback.print_exc()
    return 0

  def get_field_size(self):
    return len(self.field_info_dict)

if __name__ == '__main__':
  print ('begin')
  print ('end')
