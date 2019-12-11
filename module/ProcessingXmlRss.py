from common import Utils
from Object.Lottery import Lottery
from Object.Channel import Channel
from Object.Item import Item

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
        print('\r\n')
        listItem.append(processItem(item))
    channelObject.items = listItem
    return channelObject

def processItem(item):
    itemObject = Item()
    title = item.find('./title').text
    description = item.find('./description').text.replace('[','\n[')
    itemObject.title = title
    itemObject.description = description
    print(itemObject.title)
    print(itemObject.description)
    return itemObject