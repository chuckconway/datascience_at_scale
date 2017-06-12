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
    unscored_words = {}
    total_term_count = 0.0

    for line in lines:
        tweet = json.loads(line)  # tweet.
        tweetText = ''


        # Check if this tweet has the text property
        if 'text' in tweet:
            tweetText = tweet['text']

        # when a tweet exists, loop through
        # each sentiment term checking for the the sentiment in the tweet
        if len(tweetText) > 0:
            tweet_words = tweetText.split()

            total_term_count = len(tweet_words) + total_term_count

            #  loop through each tweet words
            for word in tweet_words:

                # remove all non Alpha numeric characters
                word = re.sub('[\W_]', '', word.lower())
                # give it a default value of 0
                occurrences = 0.0

                # check to see if the word is already a part of the unscored_words collection
                # if it does not already exist, an exception will throw.
                my_value = unscored_words.get(word)

                # if we find that it already has a value, then get the current word_score
                if my_value is not None:
                    existing_word = unscored_words[word]

                    # extract the current word score and count
                    occurrences = existing_word['occurrences']

                word_count = occurrences + 1

                # add the current word score with the new score
                unscored_words[word] = { 'occurrences': word_count}


    for key, value in unscored_words.iteritems():
        print key + ' ', round(value['occurrences'] / total_term_count, 20)


def main():
    tweet_file = open(sys.argv[1])

    printScores(tweet_file)

if __name__ == '__main__':
    main()
