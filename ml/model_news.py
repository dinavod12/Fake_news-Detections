import pickle  
import snscrape.modules.twitter as sntwitter
from joblib import  load
from datetime import datetime, timedelta
presentday = datetime.now()
yesterday = presentday - timedelta(1)

 
vectorizer = pickle.load(open(r'C:\Users\Rudra\Desktop\cv_fake.pkl',"rb"))
model_file = pickle.load(open(r'C:\Users\Rudra\Desktop\model_fake.pkl',"rb"))
#model = load(r'C:\Users\Rudra\Desktop\model_LR.joblib') 
#vector = load(r'C:\Users\Rudra\Desktop\vectorizer.joblib') 

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

corpus = []
lst1,lst2,lst3= [],[],[]

def stemming(val):
    review = re.sub('[^a-zA-Z]', ' ', val)
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    return review

def func_convert(val):
    val1 = re.sub(r"http\S+", "", val)
    return re.sub('[^a-zA-Z0-9]+', '', val1)

def func_tweets(val,lst):
    query = val
    count = 300
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        values = stemming(tweet.content)
        #print("value---",values)
        #lst.append(func_convert(values))
        lst.append(values)
        #lst.append([tweet.user.username,tweet.content,tweet.date])
        if count == len(lst):
            break 

def fake_news(data):
    news = stemming(data)
    new_form = vectorizer .transform([news])
    val = model_file.predict(new_form)
    if val[0] == 0:
        return "Real"
    else:
        func_tweets(f"(from:ANI OR from:Digital) until:{presentday.strftime('%Y-%m-%d')} since:{yesterday.strftime('%Y-%m-%d')}",lst1)
        func_tweets(f"(from:ANI) until:{presentday.strftime('%Y-%m-%d')} since:{yesterday.strftime('%Y-%m-%d')}",lst2)
        #func_tweets(f"(from:ANI OR from:Digital) until:{presentday.strftime('%Y-%m-%d')} since:{presentday.strftime('%Y-%m-%d')}",lst1)
        #func_tweets(f"(from:ANI) until:{presentday.strftime('%Y-%m-%d')} since:{presentday.strftime('%Y-%m-%d')}",lst2)
        #func_tweets("ANI Digital",lst1)
        #func_tweets("ANI",lst2)
        #func_tweets("PIB Fact Check",lst3)
        lst_all = lst1+lst2+lst3
        #lst_all = lst1
        print("length ----",len(lst_all))
        print("data ----",data)
        val1 = stemming(data)
        #val_news = func_convert(val1)
        #val_news = func_convert(data)
        #print("val_news----",val_news)
        print("val1 ----",val1)
        print("lst_all",lst_all)
        if val1 in lst_all:
            print("val_news----",val1)
            return "Real"
        else:
            return "Fake"

