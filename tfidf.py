import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def TFIDF(data, col):
  #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
  tfidf = TfidfVectorizer(stop_words='english')
  #Construct the required TF-IDF matrix by fitting and transforming the data
  tfidf1 = tfidf.fit_transform(data[col])
  return tfidf1
