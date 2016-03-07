import sys
import json
import nltk
import unicodedata
import re

def removePOS(text):
    text=nltk.word_tokenize(text)
    pos=nltk.pos_tag(text)
    list=[]
    for keys in pos:
        if keys[1]=='NN' or keys[1]=='VB':
            w=unicodedata.normalize('NFKD',keys[0]).encode('ascii','ignore')
            list.append(w)
    return list

def filterTweet(et):
    # Remove punctuations and non-alphanumeric chars from each tweet string
    pattern = re.compile('[^A-Za-z0-9]+')
    et = pattern.sub(' ', et)
    #print encoded_tweet
    words = et.split()
    # Filter unnecessary words
    for w in words:
        if w.startswith("RT") or w.startswith("www") or w.startswith("http"):
            words.remove(w)
    # print words
    return words

def calculate_frequency(file):
    newList={}
    numberOfWordsInTweets=0
    for tweet in file:
        j_tweet=json.loads(tweet)
        if 'lang' in j_tweet.keys() and j_tweet['lang']=='en':
            if 'text' in j_tweet.keys():
                # newTweets=removePOS(j_tweet['text'])
                text = unicodedata.normalize('NFKD', j_tweet["text"]).encode('ascii','ignore')
                for t in filterTweet(text):
                    numberOfWordsInTweets=numberOfWordsInTweets+1
                    if t not in newList:
                        newList.update({t:1})
                    else:
                        newList[t]=newList[t]+1
    for t in newList:
        newList[t]=(float(newList[t]))/numberOfWordsInTweets
    # print newList
    # print numberOfWordsInTweets
    return newList

def print_result(dict_result):
	for x in dict_result:
		print (x +' ' + str(dict_result[x]))
def main():
    tweet_file = open(sys.argv[1])
    result=calculate_frequency(tweet_file)
    print_result(result)



if __name__ == '__main__':
    main()
