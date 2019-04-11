# -*- coding: utf-8 -*-
import base64
# pip install pycrypto
from Crypto.Cipher import AES


class VChatAes(object):
    def __init__(self,key,vector):
        self.secret_key = key
        self.initial_vector = vector 
        self.mode = AES.MODE_CBC
        self.block_size = len(self.secret_key)
        self.cryptor = AES.new(self.secret_key, self.mode, self.initial_vector)

    def pkcs5padding(self, encoded_text):
        padding_str_len = self.block_size - len(encoded_text) % self.block_size
        padding_str = chr(padding_str_len) * padding_str_len
        return encoded_text + padding_str.encode('UTF-8')

    def pkcs5unpadding(self, padding_text):
        padding_str_len = ord(padding_text[-1])
        return padding_text[0:-padding_str_len]

    def encrypt(self, text):
        cryptor = AES.new(self.secret_key, self.mode, self.initial_vector)
        encode_text = text.encode('UTF-8')
        padding_text = self.pkcs5padding(encode_text)
        encrypt_text = cryptor.encrypt(padding_text)
        base64_text = base64.b64encode(encrypt_text)
        return base64_text

    def decrypt(self, base64_text):
        cryptor = AES.new(self.secret_key, self.mode, self.initial_vector)
        encrypt_text = base64.b64decode(base64_text)
        padding_text = cryptor.decrypt(encrypt_text)
        decode_text = padding_text.decode('UTF-8')
        text = self.pkcs5unpadding(decode_text)
        return text

if __name__ == '__main__':
    v_chat_aes = VChatAes()
    text = "winter is comming."
    encrypt_text = v_chat_aes.encrypt(text)
    orginal_text = v_chat_aes.decrypt(encrypt_text)
    print(text)
    print(encrypt_text)
    print(orginal_text)
