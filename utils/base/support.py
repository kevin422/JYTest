# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/26 16:52
# @Author  : wangqunsong
# @Email   : wangqunsong@hotmail.com
# @File    : support.py
# @Software: PyCharm
"""

import hashlib
from utils.log import logger

class EncryptError(Exception):
    pass

def sign(sign_dict, private_key=None, encrypt_way='SHA1'):
    '''
    传入待签名的字典，返回签名后字符串
    :param sign_dict:待签名的字典
    :param private_key:加密私钥
    :param encrypt_way:签名方式
    :return:签名后字符串
    '''
    dict_keys = sign_dict.keys()
    dict_keys.sort()

    string = ''
    for key in dict_keys:
        if sign_dict[key] is None:
            pass
        else:
            string += '{0}={1}&'.format(key, sign_dict[key])
    string = string[0:len(string) - 1]
    string = string.replace(' ', '')

    return encrypt(string, salt=private_key, encrypt_way=encrypt_way)


def encrypt(string, salt='', encrypt_way='SHA1'):
    u"""根据输入的string与加密盐，按照encrypt方式进行加密，并返回加密后的字符串"""
    string += salt
    if encrypt_way.upper() == 'MD5':
        hash_string = hashlib.md5()
    elif encrypt_way.upper() == 'SHA1':
        hash_string = hashlib.sha1()
    else:
        logger.exception(EncryptError('请输入正确的加密方式，目前仅支持 MD5 或 SHA1'))
        return False

    hash_string.update(string.encode())
    return hash_string.hexdigest()

if __name__ == '__main__':
    private_key = '12345678'
    sign_dict = 'Hello World!测试'
    print(encrypt(string=sign_dict, salt=private_key, encrypt_way='SHA1'))
    #print(sign(sign_dict=sign_dict, private_key=private_key, encrypt_way='SHA1'))