import sys
import json
import unicodedata
import nltk

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

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

def removePOS(text):
    # words = text.split()
    # text = [word for word in text.split() if word.startswith('@') or word.startswith('//')]
    # print text
    text=nltk.word_tokenize(text)
    text = [word for word in text if not word.startswith('@') and not word.startswith('//')]
    pos=nltk.pos_tag(text)
    list=[]
    # print pos
    for keys in pos:
        if keys[1]=='JJ' or keys[1]=='VB':
            # w=unicodedata.normalize('NFKD',keys[0]).encode('ascii','ignore')
            list.append(keys[0])
    return list

def get_sentiment(tweet_text,word_sentiment):
    words = tweet_text.split(" ")
    sentiment = 0
    for word in words:
        if word.isalpha() and word in word_sentiment.keys():
            # print str(word_sentiment[word]) + " "+ word
            sentiment += word_sentiment[word]
    return sentiment

def new_output(input_dict):
    for key in input_dict:
        print ("%s %s",(key,input_dict[key]))

def get_sentiment_of_new_words(sent_file,tweet_file):
    sentiment_of_words = get_affin_dict(sent_file)
    new_words = {}
    tweet_sentiment_dict = {}
    for tweet in tweet_file:
        tweet_json = json.loads(tweet)
        if "text" in tweet_json.keys():
                if tweet_json["lang"] == "en":
                    text = tweet_json["text"]
                    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
                    value = get_sentiment(text,sentiment_of_words)
                    # print("Total score for %s is %s  " % (tweet_json["text"], value))
                    tweet_sentiment_dict[text] = value
    # print tweet_sentiment_dict
    for key in tweet_sentiment_dict:
        words = removePOS(key)
        for w in words:
            if w not in sentiment_of_words:
                if w not in new_words:
                    if tweet_sentiment_dict[key] > 0:
                        new_words[w] = [1]
                    elif tweet_sentiment_dict[key]< 0:
                        new_words[w] = [0]
                        new_words[w].append(-1)
                else:
                    if tweet_sentiment_dict[key] > 0:
                        new_words[w][0] += 1
                    elif tweet_sentiment_dict < 0:
                        new_words[w][1] -=1
    print_output(new_words)
    return

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    get_sentiment_of_new_words(sent_file,tweet_file)
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
