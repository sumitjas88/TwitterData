import sys
import json
import nltk
import unicodedata

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def sentiments(afinnfile):
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
  		term, score  = line.split("/")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.
	return scores

def removePOS(text):
    text=nltk.word_tokenize(text)
    pos=nltk.pos_tag(text)
    list=[]
    for keys in pos:
        if keys[1]=='NN' or keys[1]=='VB':
            w=unicodedata.normalize('NFKD',keys[0]).encode('ascii','ignore')
            list.append(w)
    return list

def up(t,list):
    if t in list.keys():
        list[t]=list[t]+1
    else:
        list.update({t:1})

def calculateTweet(tweet,senti):
    count=0
    for t in tweet:
        if t in senti.keys():
            count = count + senti[t]
    return count

def calculate_sentiments(senti,tweets_fp):
    newList={}
    answer=[]
    for tweet in tweets_fp:
        j_tweet=json.loads(tweet)
        if 'lang' in j_tweet.keys() and j_tweet['lang']=='en':
            if 'text' in j_tweet.keys():
                newTweets=removePOS(j_tweet['text'])
                tweeet_score=calculateTweet(newTweets,senti)
                for t in newTweets:
                    if t not in senti.keys():
                        up(t,newList)
                        newList[t]=newList[t]-tweeet_score
    return newList




def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment=sentiments(sent_file)
    result=calculate_sentiments(sentiment,tweet_file)
    print result



if __name__ == '__main__':
    main()
