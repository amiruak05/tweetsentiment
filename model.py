import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('airline_tweets.csv')

data = df[['airline_sentiment','text']]

X = data['text']

y = data['airline_sentiment']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words='english')

tfidf.fit(X_train)

X_train_tfidf = tfidf.transform(X_train)

X_test_tfidf = tfidf.transform(X_test)

X_train_tfidf

from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train_tfidf, y_train)

from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train_tfidf, y_train)

from sklearn.svm import SVC, LinearSVC

rbf_svc = SVC()
rbf_svc.fit(X_train_tfidf,y_train)

linear_svc = LinearSVC()
linear_svc.fit(X_train_tfidf, y_train)

from sklearn.metrics import plot_confusion_matrix, classification_report

# Let's make a funtion that will always do the task for us
def report(model):
    preds = model.predict(X_test_tfidf)
    print(classification_report(y_test,preds))
    plot_confusion_matrix(model,X_test_tfidf,y_test)

report(nb)

report(log_model)

report(rbf_svc)

from sklearn.pipeline import Pipeline


# This is pipeline that will vectorize our data and apply the SVC to it
tweet_class = Pipeline([('tfidf', TfidfVectorizer()),
                ('scv',LinearSVC())])

tweet_class.fit(X,y)

import pickle
pickle_out = open("tweet_classifier.pkl", "wb")
pickle.dump(tweet_class, pickle_out)
pickle_out.close()