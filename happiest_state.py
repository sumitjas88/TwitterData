import sys
import json
import unicodedata

states = {
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

def get_affin_dict(sentiment_file):
    word_sentiment = {}
    # file_length = len(sentiment_file.readlines())
    # print file_length
    for line in sentiment_file:
        line.rstrip()
        word , value = line.split("/")
        # print word + " " + value
        word_sentiment[word] = int(value)
    return  word_sentiment

def get_tweet_sentiment(tweets_sentiments,text):
    text = unicodedata.normalize('NFKD',text).encode('ascii','ignore')
    # print text
    return sum(tweets_sentiments.get(word,0) for word in text.split())

def get_place_of_tweet(tweet_json):
    state = "none"
    if tweet_json["place"] and tweet_json["place"]["country_code"] == "US":
        # print tweet_json["place"]["country_code"] + " " + tweet_json["place"]["full_name"]
        if tweet_json["place"]["full_name"].split(',')[1]:
            state =  tweet_json["place"]["full_name"].split(',')[1]
    return state.strip()


def get_happiest_US_state(tweets_sentiments,tweet_file):
    state_dict = {}
    state_dict = dict.fromkeys(states.keys())
    # print state_dict["NC"] + 5
    # print state_dict[""]
    # print state_dict
    for tweet in tweet_file:
        tweet_json = json.loads(tweet)
        if "text" in tweet_json.keys() and tweet_json["lang"] == "en":
            value = get_tweet_sentiment(tweets_sentiments,tweet_json["text"])
            state = get_place_of_tweet(tweet_json)
            if state != "none" and len(state) == 2:
                state = unicodedata.normalize('NFKD',state).encode('ascii','ignore')
                if state_dict[state]:
                    # print str(state_dict[state]) + " ******************* " + state
                    state_dict[state] += value
                    # print str(state_dict[state]) + " &&&&&&&&&&&&&&&&&&& " + state
                else:
                    state_dict[state] = value
    k = max(state_dict, key=state_dict.get)
    print k


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    get_happiest_US_state(get_affin_dict(sent_file), tweet_file)

if __name__ == '__main__':
    main()
