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

def printScores(sentiment, tweets):
    lines = tweets.readlines()
    unscored_words = {}

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
            tweet_words = tweetText.split()

            for key, value in sentiment.iteritems():
                if key in tweetText.encode('utf-8'):
                    score = score + value

            #  loop through each tweet words
            for word in tweet_words:

                # remove all non Alpha numeric characters
                word = re.sub('[\W_]', '', word.lower())

                # check that the work is not already a sentiment
                if word not in sentiment:
                    # give it a default value of 0
                    total_score = 0
                    occurrences = 0

                    # check to see if the word is already a part of the unscored_words collection
                    # if it does not already exist, an exception will throw.
                    my_value = unscored_words.get(word)

                    # if we find that it already has a value, then get the current word_score
                    if my_value is not None:
                        existing_word = unscored_words[word]

                        # extract the current word score and count
                        total_score = existing_word['total_score']
                        occurrences = existing_word['occurrences']

                    word_total_score = total_score + score
                    word_count = occurrences + 1

                    word_score = 0.0

                    if word_total_score > 0:
                        word_score = float(word_total_score) / float(word_count)

                    # add the current word score with the new score
                    unscored_words[word] = {'total_score': word_total_score, 'average_score': word_score, 'occurrences': word_count}


    for key, value in unscored_words.iteritems():
        print key + ' ', value['average_score']


def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = getSentiment(sentiment_file)

    printScores(scores, tweet_file)

if __name__ == '__main__':
    main()
