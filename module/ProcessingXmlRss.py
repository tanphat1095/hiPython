from common import Utils


def processRss(url):
    xmlDocument = Utils.getRequestXML(url)
    channels = xmlDocument.xpath('//channel')
    for channel in channels:
        processChannel(channel)

def processChannel(channelXml):
    title = channelXml.find('./title').text
    print(title)
    for item in channelXml.xpath('./item'):
        print('\r\n')
        processItem(item)

def processItem(item):
    title = item.find('./title').text
    print(title)
    pubDate = item.find('./pubDate').text
    print(pubDate)
    description = item.find('./description').text
    print(description)