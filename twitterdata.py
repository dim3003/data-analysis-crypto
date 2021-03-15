import twint
import nest_asyncio
import datetime as dt

nest_asyncio.apply()
# Configure

TWITTER_USERNAMES = {
    'ts':'traderstewie',
    'tcl':'the_chart_life',
    'c2u':'canuck2usa',
    'st': 'sunrisetrader',
    'tt': 'tmltrader',
    'wsb': "wallstreetbets"
}
    
# for key, value in TWITTER_USERNAMES.items():

#     c = twint.Config()
#     c.Username = value
#     c.Lang = "en"
#     #c.Geo = "48.880048,2.385939,5km"
#     c.Limit = 3200
#     c.Output = f"db/tweets/{key}/{key}_{dt.date.today()}.json"
#     c.Store_json = True
#     c.Hide_output = True
    
#     tweets = twint.run.Search(c)

c = twint.Config()


c.Search = "Bitcoin"
#c.Limit = 10
c.Custom["tweet"] = ["id", "created_at","username","tweet"]
c.Verified = True
c.Lang = "en"
c.Min_likes = 500 # min like pour que le tweet soit sélectionner
c.Min_replies = 200 # min replies
c.Min_retweets = 100 # min retweets
c.Output = f"bitcoin.json"
c.Since = "2020-01-12"
c.Until = "2021-01-01"
c.Store_json = True
c.Hide_output = False
    
tweets = twint.run.Search(c)