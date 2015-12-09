from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
##ckey = 'xWSJ00HHasfaHP8YDvmhCmTdqA'
##csecret = 'eF3oTgafZUs7ZCTHXyaI7g2krrpvf2LaWf6sSIlQaww'
##atoken = '1401204486-k0fGslaW87Op0MsPYYi2vcstRj0s1HNhVyDSKAB44P'
##asecret = 'Pi60VAcdaby409frT61gvllsYixNhZassDimklSb9Y3F8'

ckey = 'uGiQ04m46736bC0BnGSav7Izz'
csecret = 'xBqeZq3IPFMV3tze52JzSfpOo5kNXVKyzq4pDT2sA2urJSYeoe'
atoken = '2832530086-xPNNUgdkxOkDRuqqyG8VMF38YdIi8mSIHRN047p'
asecret = 'zavFqT5JLO8tgDKTQ5iZnKnJSZF0TaHQ5CzIiQmvVC3EG'

class listener(StreamListener):

    def on_data(self, data):
##        print data
        jdata = json.loads(data)
##        print jdata
        print jdata['text']
        print jdata['user']['name']
        import codecs
##        with codecs.open('data1.txt','a','utf-8') as myf:
##            
##            myf.write(str(jdata['text']).encode('utf-8') + '\n')
##            myf.write(str(jdata['user']['name']).encode('utf-8') + '\n')
##        print list(jdata.keys())
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["software patent","patent assertion","patent freedom","combat patent","patent lawsuit","patent infringment","patent debate","consumer electronics association","patent reform","patent stifle innovation"])
##twitterStream.filter(track=["patent"])
