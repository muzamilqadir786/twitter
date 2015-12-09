from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import tweepy
import csv

#Handling Unicdoe
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


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

f = open('tweets.csv','a+b') 
csvwriter = csv.DictWriter(f,['User','Tweet'])
csvwriter.writeheader()

class listener(StreamListener):
    
    def on_data(self, data):        
        tweet = {}
        jdata = json.loads(data)
        tweet['Tweet'] = jdata['text'].encode('utf-8')
        tweet['User'] = jdata['user']['name']  
        print tweet      
        csvwriter.writerow(tweet)
        return True

    def on_error(self, status):
        print status

def main():
    if len(sys.argv) < 2:
        print 'usage: ./twitter.py keywords(Comma Separated Strings) \n Exp: python twitter.py "patent assertion,patent freedom" '
        sys.exit(1)

    track = sys.argv[1].split(',') 
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=track)
    # twitterStream.filter(track=["software patent","patent assertion","patent freedom","combat patent","patent lawsuit","patent infringment","patent debate","consumer electronics association","patent reform","patent stifle innovation"])

if __name__ == '__main__':
    main()



