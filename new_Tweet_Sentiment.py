import sys
import json
import unicodedata

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

def get_sentiment(tweet_text,word_sentiment):
    words = tweet_text.split(" ")
    sentiment = 0
    for word in words:
        if word.isalpha() and word in word_sentiment.keys():
            # print str(word_sentiment[word]) + " "+ word
            sentiment += word_sentiment[word]
    return sentiment

def calculate_sentiments_of_tweets(word_sentiment, tweets_file):
    count = 0
    senti_tweet = {}
    for tweet in tweets_file:
        tweet_json = json.loads(tweet)
        count+=1
        if "text" in tweet_json.keys():
                if tweet_json["lang"] == "en":
                    text = unicodedata.normalize('NFKD', tweet_json["text"]).encode('ascii','ignore')
                    value = get_sentiment(text,word_sentiment)
                    # print("Total score for %s is %s  " % (tweet_json["text"], value))
                    # print value
                    senti_tweet[text] = value
    return senti_tweet

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    sentiment_of_words = get_affin_dict(sent_file)
    return calculate_sentiments_of_tweets(sentiment_of_words, tweet_file)

if __name__ == '__main__':
    main()
