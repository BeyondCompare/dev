#coding = 'utf8'

def is_chinese(uchar): 
  if uchar >= u'\u4e00' and uchar<=u'\u9fa5': 
    return True
  return False

def is_english(uchar):
  if (uchar >= 'a' and uchar <= 'z') or (uchar > 'A' and uchar < 'Z'):
    return True
  return False

def all_chinese(word):
  for i in range(len(word)):
    if not is_chinese(word[i]):
      return False
  return True

def all_english(word):
  for i in range(len(word)):
    if not is_english(word[i]):
      return False
  return True

def all_digit(word):
  for i in range(len(word)):
    if not word[i].isdigit():
      return False
  return True

def chinese_digit(word):
  for i in range(len(word)):
    if not is_chinese(word[i]) and not word[i].isdigit():
      return False
  return True

def english_digit(word):
  for i in range(len(word)):
    if not is_english(word[i]) and not word[i].isdigit():
      return False
  return True

def chinese_english(word):
  for i in range(len(word)):
    if not is_chinese(word[i]) and not is_english(word[i]):
      return False
  return True

def chinese_english_digit(word):
  for i in range(len(word)):
    if not is_chinese(word[i]) and not is_english(word[i]) and not word[i].isdigit():
      return False
  return True

def lang_detect(word):
  if all_chinese(word):
    return 1
  if all_digit(word):
    return 2
  if all_english(word):
    return 3
  if chinese_digit(word):
    return 4
  if english_digit(word):
    return 5
  if chinese_english(word):
    return 6
  if chinese_english_digit(word):
    return 7
  return 8

if __name__ == '__main__':
  print ('begin')
  s = 'p图app'
  print (lang_detect(s))
  print ('end')