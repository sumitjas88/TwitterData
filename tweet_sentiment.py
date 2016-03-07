import sys
import json

def sentiments(sent_file):
	afinnfile = open("AFINN-111.txt")
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
  		term, score  = line.split("/")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.
  		# print term + " " + score

	return scores # Print every (term, score) pair in the dictionary

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def ans(answer):
	len=0
	for i in answer:
		print answer[i] + " " + len
		len=len+1



def calculate_sentiments(tweets,sent_file):
	senti=sentiments(sent_file)
	anss=[]
	for tweet in tweets:
		count=0
		for word in tweet.split(" "):
			if word.isalpha():
				if word in senti:
					count = count + senti[word]
		anss.append(count)
	ans(anss)

def convert_keys_to_string(dictionary):
    """Recursively converts dictionary keys to strings."""
    if not isinstance(dictionary, dict):
        return dictionary
    return dict((str(k), convert_keys_to_string(v))
        for k, v in dictionary.items())
def main():
    sent_file = open(sys.argv[1])
    with open(sys.argv[2]) as tweet_file :
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    # sentiments(sent_file)
	    tweets=[]
	    answer=[]
	    for line in tweet_file:
	    	tweet=json.loads(line)
	    	tweet_of_dict = convert_keys_to_string(tweet)
	    	print type(tweet_of_dict)
	    	print tweet_of_dict['u\'text']
	    	if 'text' in tweet:
				print tweet['text']
				tweets.append(tweet['text'])
		calculate_sentiments(tweets,sent_file)

if __name__ == '__main__':

    main()
