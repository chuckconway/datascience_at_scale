import sys
import json

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

def printScores(sentiment, tweets):
    lines = tweets.readlines()

    for line in lines:
        tweet = json.loads(line)  # tweet.
        score = 0
        tweetText = ''

        # Check if this tweet has the text property
        if 'text' in tweet:
            tweetText = tweet['text']

        # when a tweet exists, loop through
        # each sentiment term checking for the the sentiment in the tweet
        if len(tweetText) > 0:
            for key, value in sentiment.iteritems():
                if key in tweetText.encode('utf-8'):
                    score = score + value

        print score


def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = getSentiment(sentiment_file)
    printScores(scores, tweet_file)

if __name__ == '__main__':
    main()
