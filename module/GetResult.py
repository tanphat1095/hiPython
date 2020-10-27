from module import ProcessingXmlRss
import json
from common import Utils
from Object.Rss import Rss
from module import firebasedb
import time

domain = 'https://xskt.com.vn'
xpath  = "//ul[@id='ulrss']/li/a"
firebase = firebasedb.initFirebase()
result = []

def __init__(self):
    ''

def getLotteryAsJSON(url):
    lottery = ProcessingXmlRss.processRss(url)
    json_ = json.dumps(lottery, default=lambda lottery : lottery.__dict__)
    # print(json.loads(json_))
    return json_

def getListRss():
    listRss = []
    xml = Utils.getRequestHTML('https://xskt.com.vn/rss/')
    listUrl = xml.xpath(xpath)
    for a in listUrl:
        link = domain + a.get('href')
        text = a.text
        rss = Rss()
        rss.title = text
        rss.url = link
        listRss.append(rss)
    return listRss
def getFullResult():
    listRss = getListRss()
    timeInt = round(int(time.time() *1000))
    ref = firebase.reference('lottery/'+ str(timeInt))
    for rss in listRss:
        print('\n'*3 +rss.title + ' - '+ rss.url)
        result = json.loads(getLotteryAsJSON(rss.url))
        ref.set(result)


