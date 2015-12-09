from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import tweepy
import csv
import sys
##
###Handling Unicdoe
import sys
##reload(sys)
##sys.setdefaultencoding("utf-8")


##############################

#       Instructions
#       Install tweepy module using pip install tweepy
#       The script will stream all the keywords and writes them to csv(Excel file), the tweet text and User
#       usage: python ./twitter.py keywords(Comma Separated Strings) \n Exp: python twitter.py "patent assertion,patent freedom"

##############################

ckey = 'uGiQ04m46736bC0BnGSav7Izz'
csecret = 'xBqeZq3IPFMV3tze52JzSfpOo5kNXVKyzq4pDT2sA2urJSYeoe'
atoken = '2832530086-xPNNUgdkxOkDRuqqyG8VMF38YdIi8mSIHRN047p'
asecret = 'zavFqT5JLO8tgDKTQ5iZnKnJSZF0TaHQ5CzIiQmvVC3EG'

"""
Authenticating Twitter 
"""
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

"""
Writing Tweets to File
"""
f = open('tweets.csv','a+b') 
csvwriter = csv.DictWriter(f,['User','Tweet'])
csvwriter.writeheader()

USERNAME = "nawazishqadir.odesk@gmail.com"  #Gmail User name 
PASSWORD = "bsef07m00004"  #Gmail password
SPREADSHEET_NAME = "Patent Troll Scraping Results" 

def GSheetService(user,pwd):
    import gdata.spreadsheet.service
    import string
    client = gdata.spreadsheet.service.SpreadsheetsService()
    client.email = USERNAME
    client.password = PASSWORD
    client.ProgrammaticLogin()
    return client

def WriteToGoogleSpreadSheet(Tweet):
    print Tweet
    client = GSheetService(USERNAME,PASSWORD)
    docs = client.GetSpreadsheetsFeed()
    spreads = []
    for spread in docs.entry:
        spreads.append(spread.title.text)

    spread_number = None
    for i,j in enumerate(spreads):
        if j == SPREADSHEET_NAME:
            spread_number = i
        else:
            spread_number = 0

    key = docs.entry[spread_number].id.text.rsplit('/', 1)[1]
    feed = client.GetWorksheetsFeed(key)
    wksht_id = feed.entry[0].id.text.rsplit('/', 1)[1]    
    feed = client.GetListFeed(key,wksht_id)
    tweets = Tweet
    for tweet in tweets:
##        print tweet
        if tweet:
            try:
                entry = client.InsertRow(tweet,key,wksht_id)
            except Exception as e:
                print e
            

class listener(StreamListener):
    
    def on_data(self, data):        
        tweet = {}
        jdata = json.loads(data)
        tweet['tweet'] = jdata['text']
        tweet['user'] = jdata['user']['name']
##        print tweet
##        csvwriter.writerow(tweet) #Uncomment if want to write on local file
        WriteToGoogleSpreadSheet([tweet])
        return True

    def on_error(self, status):
        print status

def searchTwitter():
    tweets = []
    for tweet in api.search(q=sys.argv[2].split(","),result_type="mixed",lang="en",count=1000):
        tweet = dict({'tweet':tweet.text, 'user':tweet.user.name})
        tweets.append(tweet)
        
    WriteToGoogleSpreadSheet(tweets)
##        csvwriter.writerow(tweet) #Uncomment if want to write on local 

def streamTwitter():
    track = sys.argv[2].split(',') 
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=track,languages = ["en"])

def main():
    if len(sys.argv) < 2:
        print 'usage: ./twitter.py [stream or search] keywords(Comma Separated Strings) \n Exp: python twitter.py "patent assertion,patent freedom" '
        sys.exit(1)

    if sys.argv[1].lower() == 'search':
        searchTwitter()
    if sys.argv[1].lower() == 'stream':
        streamTwitter()
        
    # twitterStream.filter(track=["software patent","patent assertion","patent freedom","combat patent","patent lawsuit","patent infringment","patent debate","consumer electronics association","patent reform","patent stifle innovation"])

if __name__ == '__main__':
    main()



