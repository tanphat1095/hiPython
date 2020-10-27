from common import Utils
from Object.Lottery import Lottery
from Object.Channel import Channel
from Object.Item import Item



def __init__(self):
    ''

def processRss(url):
    lottery = Lottery()
    listChannel = []

    xmlDocument = Utils.getRequestXML(url)
    channels = xmlDocument.xpath('//channel')
    for channel in channels:
        listChannel.append(processChannel(channel))
    lottery.channels = listChannel
    return lottery

def processChannel(channelXml):
    channelObject = Channel()
    listItem = []
    for item in channelXml.xpath('./item'):
        listItem.append(processItem(item))
    channelObject.items = listItem
    return channelObject


def processDetails(description):
    details = {}
    arr = description.split('\n\n')
    arr2 = [x for x in arr if x != '']
    for arr_ in arr2:
        arr_detail = arr_.split('\n')
        province = Utils.remove_accents(arr_detail[0].replace('[','').replace(']','').strip())
        detail = {}
        for i in range(1,len(arr_detail)):
            detailItem = arr_detail[i].split(':')
            key = detailItem[0].strip()
            value = detailItem[1].strip()
            detail[str(key)] = value
        details['detail'] = detail
        details['province'] = province
    return details


def processItem(item):
    itemObject = Item()
    title = item.find('./title').text
    description = item.find('./description').text.replace('[','\n[')
    itemObject.title = title
    itemObject.details = processDetails(description)
    return itemObject