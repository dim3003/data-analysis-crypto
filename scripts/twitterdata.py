import twint
#import nest_asyncio
import datetime as dt

#nest_asyncio.apply()


TWITTER_USERNAMES = {
    'ts':'traderstewie',
    'tcl':'the_chart_life',
    'c2u':'canuck2usa',
    'st': 'sunrisetrader',
    'tt': 'tmltrader',
    'wsb': "wallstreetbets"
}

if __name__ == '__main__':

    #select keywords for each crypto we will train our model on

    names = []

    bitcoin = ["BTC", "Bitcoin", "bitcoin"]
    names.append(bitcoin)
    ethereum = ["ETH", "Ethereum", "ethereum"]
    names.append(ethereum)
    eos = ["EOS"]
    names.append(eos)

    #look for tweets for each crypto
    for i in names:
        name = i
        c = twint.Config()

        c.Search = name
        c.Custom["tweet"] = ["id", "created_at","username","tweet"]
        c.Verified = True
        c.Lang = "en"
        c.Min_replies = 10 # min replies
        c.Output = f"../data/raw/{name[0]}.json"
        c.Since = "2017-08-17"
        c.Until = "2021-04-19"
        c.Store_json = True
        c.Hide_output = False

        tweets = twint.run.Search(c)
