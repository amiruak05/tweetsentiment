# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle

#app = Flask(__name__)

pickle_in = open('tweet_classifier.pkl', 'rb')
tweet_classifier = pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome to the Tweet Classifier"

#@app.route('/predict')
def predict_tweet_class(tweet_class):
    prediction = tweet_classifier.predict([tweet_class])
    print(prediction)
    return prediction

#@app.route('/predict_file', methods=["POST"])
def main():
    st.title("Sentiment Detector")
    html_temp = """
    <div style="backgroud-color:tomato;padding:10px>"
    <h2 style="color:white;text-align:center;">Tweet Sentiment Detector </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    tweet_class = st.text_input("write a tweet about your flight experience","tweet")
    result=""
    if st.button("Predict"):
        result=predict_tweet_class(tweet_class)
    st.success("Your sentiment is {}".format(result))
    if st.button("About"):
        st.text("This page was built with Streamlit by Amiru")
    

if __name__ == '__main__':
    main()