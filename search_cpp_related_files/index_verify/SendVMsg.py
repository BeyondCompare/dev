import json
import requests
import configparser
import os
from VChatAes import VChatAes
"""
aes = VChatAes()
headers = {'Content-type': 'application/json'}
data = {'fromUserCode': '发送者工号', 'toUserCode': aes.encrypt('接收者工号').decode('UTF-8'), 'msgText': aes.encrypt('V消息接口测试').decode('UTF-8')}
url = 'http://vchat.vivo.xyz:8088/vivo/com.sie.mp.chatmsg.exter.sendMsgToMutilUsers.biz.ext'
response = requests.post(url, data=json.dumps(data), headers=headers)
"""
class SendVMsg(object):
	def __init__(self,msg):
		self.msg = msg

	def get_conf_file(self):
		cur_path = os.getcwd()
		conf_file = os.path.join(cur_path,"..","conf","v_msg_conf")
		return conf_file

	def load_conf(self,section,option):
		conf_file = get_conf_file()
		cp = configparser.ConfigParser()
		cp.read(conf_file)
		return cp.get(section,option)

	def aes_encypt(self,ori_input):
		key = load_conf("aes","key")
		vector = load_conf("aes","vector")
		aes = VChatAes(key,vector)
		proc_res = aes.encrypt(ori_input)
		return proc_res

	def get_aes_res(self,ori_input):
		proc_res = aes_encrypt(ori_input)
		return proc_res

	def get_from_code(self):
		from_code = load_conf("code","fromUserCode")
		return from_code

	def get_to_code(self):
		ini_to_code = load_conf("code","toUserCode")
		to_code = get_aes_res(ini_to_code)
		return to_code.decode('UTF-8')
		
	def get_encrypt_msg(self):
		enc_msg = get_aes_res(self.msg)
		return enc_msg.decode('UTF-8')

	def get_inner_url(self):
		url = load_conf("url","url")
		return url

	def get_inner_data(self):
		from_code = get_from_code()
		to_code = get_to_code()
		enc_msg = get_encrypt_msg()
		in_f_code = "'" + "fromUserCode" + "'" + ":" + "'" + from_code + "'"
		in_to_code = "'" + "toUserCode" + "'" + ":" + "'" + to_code + "'"
		in_msg = "'" + "msgText" + "'" + ":" + "'" + enc_msg + "'"
		inner_data = in_f_code + ',' + in_to_code + ',' + in_msg
		return inner_data

	def send_v_msg(self):
		headers = {'Content-type': 'application/json'}
		url = get_inner_url()
		inner_data = get_inner_data()
		# 不确定 从inner_data到data的转换是否ok
		data ='{' + inner_data + '}'
		response = requests.post(url, data=json.dumps(data), headers=headers)
		if response == 'S':
			return 0
		else:
			return -1







