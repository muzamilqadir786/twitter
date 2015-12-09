import json
from pyquery import PyQuery
import time
import urllib
import urllib2

def getUrlData(url, retries=5, sleepTimeout=5):
    for i in xrange(retries):
        try:
            opener = urllib2.build_opener()
            opener.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11")]
            response = opener.open(url)
            return response.read()
        except:
            time.sleep(sleepTimeout)
 
    return None

def parseNumber(num):
    num = num.replace(",", "")
    if num[-1] == "k":
        return int(float(num[:-1]) * 1000)
    else:
        return int(num)

def getLikeCount(url):
    url = "http://www.facebook.com/plugins/like.php?api_key=&locale=en_US&sdk=joey&channel_url=&href=%s&node_type=link&width=90&layout=button_count&colorscheme=light&show_faces=false&send=false" % urllib.quote_plus(url)
 
    d = PyQuery(getUrlData(url))
    return parseNumber(d.find("span.pluginCountTextDisconnected").text())
 
def getTweetCount(url):
    url = "http://cdn.api.twitter.com/1/urls/count.json?url=%s" % urllib.quote_plus(url)
 
    data = getUrlData(url)
    return parseNumber(str(json.loads(data)["count"]))
 
def getGPlusCount(url):
    url = "https://plusone.google.com/_/+1/fastbutton?bsv&url=%s" % urllib.quote_plus(url)
 
    d = PyQuery(getUrlData(url))
    return parseNumber(d.find("#aggregateCount").text()) 
 
def getLinkedinCount(url):
    try:
        url = "http://www.linkedin.com/countserv/count/share?url=%s&lang=en_US" % urllib.quote_plus(url)
     
        linkedin_data = getUrlData(url)
        linkedin = json.loads(linkedin_data[26:-2])
        return linkedin["count"]
    except Exception, ex:
        print ex
        print url
 
        return 0

def searchTweets(url="https://api.twitter.com/1.1/search/tweets.json/?"):
##    url = "https://api.twitter.com/1.1/search/tweets.json/?"
    searchquery = urllib.urlencode({"q":"politics","count":"100","result_type":"popular","lang":"en"})
    data = getUrlData(url+searchquery)
    print data

##print searchTweets()

##data = getUrlData('https://www.googleapis.com/youtube/v3/search?part=snippet&q=patent&type=video&videoCategoryId=10&maxResults=20&key=AIzaSyC1OBxvglmaEoX0zNwqpxsnZ2cnsPRyJuM')
##import json
##jdata = json.loads(data)
##snippets = jdata["items"]
##print snippets
##channelIds = []
##for snippet in snippets:
##    print snippet['snippet']
##    print snippet["snippet"]["description"]
##    print snippet["snippet"]["title"]
##    
##    channelIds.append(snippet["snippet"]["channelId"])
##print channelIds
##print len(channelIds)
##print list(set(channelIds))
##print len(list(set(channelIds)))

##ids = ','.join(list(set(channelIds)))
##print ids
##import urllib
##ids = urllib.urlencode({'id':ids})
####url = 'https://www.googleapis.com/youtube/v3/channels?part=snippet&'+ids
####url = 'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&key=AIzaSyC1OBxvglmaEoX0zNwqpxsnZ2cnsPRyJuM'
url = "https://www.googleapis.com/youtube/v3/search?key=AIzaSyC1OBxvglmaEoX0zNwqpxsnZ2cnsPRyJuM&channelId=UCHkj014U2CQ2Nv0UZeYpE_A&part=snippet,id&order=date&maxResults=20"
print url
mdata = getUrlData(url)
print mdata

