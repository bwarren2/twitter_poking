## Twitter poking

Poking at the twitter API, to see what there is to see.

### Installation

`mkvirtualenv whateverenv`
`workon whateverenv`
`pip install -r requirements.txt`

```
export CONSUMER_PUBLIC_KEY=redacted
export CONSUMER_PRIVATE_KEY=redacted
export ACCESS_TOKEN=redacted
export ACCESS_TOKEN_SECRET=redacted
```

`python stream.py --term Trump`


### Initial conclusions:

There is not much geo data to work with.  Very few messages actually have it.  Similary for location.

Initial textual analysis is hard, because the argots of twitter are unique (ex lots of abbreviations).  There is a preliminary cut of sentiment analysis in place in the stream output, but it frequently returns empty for tweets; I am not confident in its viability as a metric.

Ex: "RT @MtnMD: RT @Taiping2 @ColMorrisDavis: @realDonaldTrump: @HillaryClinton is "horrible human being." Grt ldrs on Trump Train. https://t.co…"

Retweet analysis: apparently the API only returns up to the first 100?

```
API.retweets(id[, count])

    Returns up to 100 of the first retweets of the given tweet.
```
-- http://docs.tweepy.org/en/v3.4.0/api.html, and [here](http://stackoverflow.com/questions/29526356/how-to-get-more-than-100-retweets-of-the-specific-tweet)

Perhaps the easiest thing would be social graphing.  `follow_both.py` will find the people that follow both Trump and Hillary and print the first few.

I am over my rate limit and shut off from the API for now, but LMK what you think.


### Basic results:
`python stream.py --term @realDonaldTrump`
Counter({'negative': 114, 'positive': 93, 'trust': 69, 'anticipation': 59, 'anger': 57, 'joy': 42, 'sadness': 40, 'fear': 35, 'disgust': 34, 'surprise': 18})


`python stream.py --term @HillaryClinton`
Counter({'negative': 117, 'positive': 87, 'anger': 68, 'anticipation': 61, 'trust': 59, 'fear': 57, 'sadness': 51, 'disgust': 47, 'joy': 24, 'surprise': 24})

`python stream.py --term Ichiro3000`
Counter({'negative': 66, 'anger': 22, 'anticipation': 17, 'positive': 16, 'surprise': 14, 'sadness': 13, 'trust': 13, 'joy': 2, 'fear': 2, 'disgust': 1})

`python stream.py --term HillaryCoverageIsCrap`
Counter({'positive': 278, 'negative': 204, 'trust': 193, 'anger': 113, 'anticipation': 98, 'fear': 93, 'sadness': 88, 'disgust': 84, 'joy': 62, 'surprise': 39})

### Potential improvements:

Better word processing than just string.split().  Currently doesn't strip punctuation, which will cause sentiment lookup failures.

Sarcasm is a big problem for this sort of analysis.

I am not sure I believe the initial results; I feel like "HillaryCoverageIsCrap" should have more negatives than positives.
