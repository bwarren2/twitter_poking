from __future__ import absolute_import, print_function
import click

import json

from os import getenv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import csv
from collections import defaultdict, Counter


@click.command()
@click.option('--term', default='Trump', help='What search string to track.')
def track(term):
    store = wordstore()

    consumer_key = getenv('CONSUMER_PUBLIC_KEY')
    consumer_secret = getenv('CONSUMER_PRIVATE_KEY')

    access_token = getenv('ACCESS_TOKEN')
    access_token_secret = getenv('ACCESS_TOKEN_SECRET')

    class StdOutListener(StreamListener):
        """ A listener handles tweets that are received from the stream.
        This is a basic listener that just prints received tweets to stdout.
        """
        def on_data(self, data):
            foo = json.loads(data)
            if foo.get('geo', None):
                print ('GEO!!!')
                print ('GEO!!!')
                print ('GEO!!!')
                print(foo)
            else:
                print(foo['text'])

            # for word in foo['text'].split():
            #     print(store[word])

            senses = [
                store[word]
                for word in foo['text'].split()
            ]
            terms = [item for sublist in senses for item in sublist]
            print(Counter(terms))

            return True

        def on_error(self, status):
            print(status)

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=[term])


def wordstore():

    store = defaultdict(list)
    with open('words.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if row[2] != '0':
                store[row[0]].append(row[1])

    return store

if __name__ == '__main__':
    track()
