# -*- coding: utf-8 -*-
"""Self_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17Svr7WlNGlvjB4ZZyaMjsuvj7NQHNCot
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('SMSSpamCollection.txt',sep='\t',   names=["label", "message"])

df.head()

# Data Cleaning and Preprocessing

import re
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

PS = PorterStemmer()

corpos  = []
for i in range(0,len(df['message'])):
    rev = re.sub('[^a-zA-Z]',' ',df['message'][i])
    rev = rev.lower()
    rev = rev.split()
    rev = [PS.stem(word) for word in rev if not word in stopwords.words('english')]
    rev = ' '.join(rev)
    corpos.append(rev)

# Using Bag of Word Feature Engineering

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=2500)

x = cv.fit_transform(corpos).toarray()

y=pd.get_dummies(df['label'])
y=y.iloc[:,1].values

# train test split

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)

# Using Naive Bayes Classifier

from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(x_train, y_train)

y_pred=spam_detect_model.predict(x_test)

from sklearn.metrics import classification_report

classification_report(y_test, y_pred)

from sklearn.metrics import f1_score
f1_score(y_test, y_pred)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

