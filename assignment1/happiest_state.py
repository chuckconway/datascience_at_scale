import sys
import json


def get_states():
    return {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

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
    state_happiness = {}
    states = get_states()

    for line in lines:
        tweet = json.loads(line)  # tweet.
        score = 0
        tweetText = ''

        if 'user' in tweet:
            user_info = tweet['user']
            location = user_info['location']

            # Check if this tweet has the text property
            if 'text' in tweet and location is not None:
                tweetText = tweet['text']

            # when a tweet exists, loop through
            # each sentiment term checking for the the sentiment in the tweet
            if len(tweetText) > 0:
                for key, value in sentiment.iteritems():
                    if key in tweetText.encode('utf-8'):
                        score = score + value

                for key, value in states.iteritems():
                    if key in location or value.lower() in location.lower():
                        instance = state_happiness.get(key)
                        total_occurances = 0.0
                        total_score = 0.0

                        if instance is not None:
                            happiness = state_happiness[key]
                            total_occurances = happiness['total_occurances']
                            total_score = happiness['total_score']

                        total_occurances = total_occurances + 1
                        total_score = total_score + score

                        state_happiness[key] = {'average_score': total_score/total_occurances, 'total_occurances':total_occurances, 'total_score': total_score}

    items = state_happiness.items()
    items.sort(key=lambda tup: tup[1])
    items.reverse()

    # for key, value in state_happiness.iteritems():
    first = items[0]
    print first[0]


def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = getSentiment(sentiment_file)

    printScores(scores, tweet_file)


if __name__ == '__main__':
    main()


