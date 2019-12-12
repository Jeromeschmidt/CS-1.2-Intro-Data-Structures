from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from sample import get_sentence
from nth_order_markov_chain import MarkovChain
from datetime import datetime
import random
import os
import re
import tweepy
from dotenv import load_dotenv
load_dotenv()

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/tweet_coll')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
tweet_coll = db.tweet_coll

#twitter api code adapted from: https://www.geeksforgeeks.org/tweet-using-python/
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update the status

app = Flask(__name__)

with open("sherlock.txt",'r') as file:
    text = file.read()
    # text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.split()
markovChain = MarkovChain(text, 2)

@app.route('/')
def index():
    sentence = markovChain.random_walk(random.randint(2, 20))
    if "red" in sentence:
        color = "red"
    else:
        color = "black"
    return render_template('index.html', sentence=sentence, color=color)

@app.route('/<sentence>', methods=['POST'])
def save_tweet(sentence):
    """saves a given phrase as a tweet in a db and tweets it out"""
    tweet = {
        'tweet_content': sentence,
        'created_at': datetime.now(),
    }
    tweet_id = tweet_coll.insert_one(tweet).inserted_id

    # ADD PIECE THAT TWEETS IT OUT
    # Create a tweet
    api.update_status(status =sentence)

    sentence = markovChain.random_walk(random.randint(2, 20))
    return redirect(url_for('index', sentence=sentence))

@app.route('/view_favorites/<tweet_id>/delete', methods=['POST'])
def delete_tweet(tweet_id):
    """Delete one tweet."""
    tweet_coll.delete_one({'_id': ObjectId(tweet_id)})
    return redirect(url_for('view_favorites'))

@app.route('/view_favorites')
def view_favorites():
    return render_template('view_favorites.html', tweets=tweet_coll.find().sort([('created_at', -1)]))

@app.route('/description')
def description():
    return render_template('description.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
