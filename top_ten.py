import sys
import json
import operator

def get_top_ten_tweets():
    tweet_file = open(sys.argv[1])
    hashtag_map = {}
    for tweet in tweet_file:
        tweet_json = json.loads(tweet)
        if "entities" in tweet_json.keys():
            entity =  tweet_json["entities"]["hashtags"]
            for e in entity:
                hashtag = e["text"]
                if hashtag_map.get(hashtag):
                    hashtag_map[hashtag] += 1
                else:
                    hashtag_map[hashtag] = 1
    result = sorted(hashtag_map.items(), key=operator.itemgetter(1))
    result.reverse()
    for key in result[:10]:
        print key[0] + " " + str(key[1])


if __name__ == '__main__':
    get_top_ten_tweets()
