import requests
from lxml import etree as ET
import threading
import time
import random
from module import ProcessingXmlRss


if(__name__ == '__main__'):

    #get lottery result with from rss with xml processing
    ProcessingXmlRss.processRss('https://xskt.com.vn/rss-feed/mien-nam-xsmn.rss')


