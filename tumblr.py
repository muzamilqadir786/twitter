import pytumblr

ckey = 'PYUntgPguP1Yc1RKwoa4b0xZVD4xlWgX5lTDzdtDmHqsjTZuaB'
csecret = 'Okxjpu1p7WuQLJ4sxxmJ3TwiTs0cXqyjawWe0TUwdRxWqJXa1G'
atoken = 'EOpYjvj8fmrvDAp0ZVWbfKibhoVj5uwlk7tEATq1bSOJgFu5Na'
asecret = 'u2XzrsLbQc9cBWQknj2KOR18ZY2GjHEV7PRlBDZm2M2DTLhOZn'

"""
Authenticating Twitter 
"""

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(ckey,csecret,atoken,asecret)

# Make the request
dashboard = client.dashboard()
print client.blog_info('software')

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
