import pickle     
cv_file = pickle.load(open(r'C:\Users\Rudra\Desktop\cv.pkl',"rb"))
model_file = pickle.load(open(r'C:\Users\Rudra\Desktop\model.pkl',"rb"))

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

corpus = []
def stemming(val):
    review = re.sub('[^a-zA-Z]', ' ', val)
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    return review
def fake_spam(data):
    news = stemming(data)
    new_form = cv_file.transform([news])
    val = model_file.predict(new_form)
    if val[0] == 0:
        print("val_news----",val)
        return "Real"
    else:
        return "Fake"
