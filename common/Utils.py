  # coding=utf-8
'''
Created on 11 thg 12, 2019
@author: phatlt
'''
import time
import requests
import urllib3
from lxml import html
from lxml import etree as ET
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s
def getRequestXML_(url,verify):
    headers = {
        'content-type': "application/x-www-form-urlencoded",   
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }
    try:
        response = requests.request("GET", url, headers=headers,timeout=(60,60),verify=verify)
        #return html.fromstring(response.content.decode(response.encoding))
        return ET.XML(response.content)
    except Exception as ex:
        print(ex)
        return None
def getRequestXML(url,verify=False):
    xml = getRequestXML_(url, verify)
    while xml == None:
        print ('Khong lay duoc ket qua')
        print ('Tu dong lay ket qua sau 5s')
        time.sleep(5)
        print ('Dang lay ket qua')
        xml = getRequestXML_(url, verify)
    return xml

def getRequestHTML_(url,verify):
    headers = {
        'content-type': "application/x-www-form-urlencoded",   
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }
    try:
        response = requests.request("GET", url, headers=headers,timeout=(60,60),verify=verify)
        return html.fromstring(response.content.decode(response.encoding))
        #return ET.XML(response.content)
    except Exception as ex:
        print(ex)
        return None

def getRequestHTML(url,verify=False):
    xml = getRequestHTML_(url, verify)
    while xml == None:
        print ('Khong lay duoc ket qua')
        print ('Tu dong lay ket qua sau 5s')
        time.sleep(5)
        print ('Dang lay ket qua')
        xml = getRequestHTML_(url, verify)
    return xml