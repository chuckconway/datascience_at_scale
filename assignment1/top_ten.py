import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def getSentiment(sentiments):
    scores = {}  # initialize an empty dictionary
    for line in sentiments:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores

def parseTweets(tweets):
    return json.loads(tweets)

def printScores(tweets):
    lines = tweets.readlines()
    hashtags = {}

    for line in lines:
        tweet = json.loads(line)  # tweet.
        tweetText = ''

        # Check if this tweet has the text property
        if 'text' in tweet:
            tweetText = tweet['text']

        # when a tweet exists, loop through
        # each sentiment term checking for the the sentiment in the tweet
        if len(tweetText) > 0:

            if 'entities' in tweet:
                hts = tweet['entities']['hashtags']

                if hts is not None:
                    for tag in hts:
                        tagText = tag['text'].lower()
                        t = hashtags.get(tagText)
                        count = 0

                        if t is not None:
                            count = hashtags[tagText]

                        hashtags[tagText] = count + 1

    items = hashtags.items()
    items.sort(key=lambda tup: tup[1])
    items.reverse()

    for item in items[:10]:
        print item[0].encode('utf-8') + ' ', item[1]


def main():
    tweet_file =  open(sys.argv[1])

    printScores(tweet_file)

if __name__ == '__main__':
    main()
