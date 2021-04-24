import pandas as pd
import numpy as np
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def processTweet(name):
    #Twitter data
    dft = pd.read_json(f"../data/raw/{name}.json", lines = True,  orient='records')

    #date formatting
    dft['date'] = pd.to_datetime(dft['created_at'])
    dft['date'] = dft['date'].dt.strftime('%Y-%m-%d')
    dft['date'] = pd.to_datetime(dft['date'])
    del dft['created_at']

    ###get top 10 users with most likes from last year

    #cut tweet db from last year & clean it
    dfft = dft.where(dft['date'] >= pd.to_datetime('2020-04-19')).dropna().drop_duplicates(subset=['tweet'])

    #get 10 most liked
    top10 = dfft.groupby(['username']).sum()
    top10 = top10.iloc[:, 1].sort_values(ascending=False)[:10]
    top10 = top10.index.values

    ###create the per day database

    #create an empty dataframe with the right columns

    dfF = pd.DataFrame(columns = ['tweet_count', 'daily_sent', 'daily_sent_blob', *top10])


    #get all unique dates
    uDate = dft.loc[:, 'date'].unique()
    dfF.insert(0, 'date', uDate)
    dfF.set_index(uDate, inplace = True)

    #create data for each date
    uDate = pd.Series(uDate)

    for i in uDate:
        dfPartial = dft.where(dft["date"] == i).dropna()

        #create number of tweets
        dfF.loc[i, 'tweet_count'] = len(dfPartial)

        #create sentiment for the day
        model = SentimentIntensityAnalyzer()
        score = []
        scoreBlob = []
        for j in dfPartial["tweet"]:
            sent_dict = model.polarity_scores(j)
            score.append(sent_dict['compound']) #vaderSentiment analysis
            scoreBlob.append(TextBlob(j).sentiment.polarity) #textblob sentiment analysis

        score = sum(score)/len(score) #daily mean sentiment vader
        scoreBlob = sum(scoreBlob)/len(scoreBlob) #daily mean sentiment blob
        dfF.loc[i, 'daily_sent'] = score
        dfF.loc[i, 'daily_sent_blob'] = scoreBlob


        #create binary in function of influencer
        for j in top10:
            if dfPartial['username'].str.contains(j).sum() > 0:
                dfF.loc[i, j] = 1
            else:
                dfF.loc[i, j] = 0
        dfF.to_csv(f"../data/processed/{name}.csv")

for i in ['BTC', 'ETH', 'EOS']:
    processTweet(i)
