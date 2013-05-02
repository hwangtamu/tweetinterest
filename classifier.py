import requests
import json
import sys
import string,re,math,random,copy
import unicodedata,os
__author__='wczhang'

target=['Business','Sports','Movies','Technology','Travel','Education','Politics','Fashion','Music','Science','Health']
interest_threshold=1/float(5)
topic_threshold=0.0009
file1='data/featureword/featureresults.json'
file2='data/featureword/lda.json'
directory='data/users/'

def load_feature(filename):
	#load dictionary from file, MI_dict[topic][word]=scroe
	f=open(filename,'r')
	for line in f:
		MI_dict=json.loads(line.replace('\r','\\r'))
	return MI_dict

def load_tweet_data(filename):
	#load tweet data from file
	f=open(filename,'r')
	for line in f:
		tweet_dict=json.loads(line.replace('\r','\\r'))
	return tweet_dict

def get_max(score):
	#return the max score of one tweet
	max_score=0
	max_topic=''
	for topic in score.keys():
		if score[topic]>max_score:
			max_score=score[topic]
			max_topic=topic
	return (max_topic,max_score)
		
def tweet_class(MI_dict,tweet_dict):
	count={}
	for term in target:
		count[term]=0
	count['']=0
	count['total']=0
	for key in tweet_dict:
		#text=line['text']
		text=tweet_dict[key]
		data=re.findall(r"[A-Za-z']+",text,flags=re.UNICODE)
		score={}
		for topic in target:
			score[topic]=0
			for word in data:
				if MI_dict[topic].get(word)!=None:
					score[topic]=score[topic]+MI_dict[topic][word]/float(MI_dict[topic]['totalscore'])
					#print word
		#print score
		max_topic,max_score=get_max(score)
		#print 'topic: ',max_topic
		count[max_topic]=count[max_topic]+1
		count['total']=count['total']+1
	#print count
	return count

def text_interest_define(count):
	interest_portion={}
	for topic in target:
		portion=count[topic]/float(count['total']-count[''])
		if portion>interest_threshold:
			interest_portion[topic]=portion
	#for keys,values in sorted(interest_portion.items(),reverse=True,key=myFN):
		#print 'interest: ',keys,' percentage: ',values
	return interest_portion
	
		
def myFN(s):
	return s[-1]			
	
def analyze_files(dir,MI_dict):
	user_dict={}
	file_names=os.listdir(dir)
	print file_names
	for file_name in file_names:
		user_id=file_name[:-5]
		tweetfile=dir+'/'+file_name
		#print tweetfile
		tweet_dict=load_tweet_data(tweetfile)
		count=tweet_class(MI_dict,tweet_dict)
		interest_portion=text_interest_define(count)
		if len(interest_portion)!=0:
			user_dict[user_id]={}
			user_dict[user_id]['text_interest']=[]		
			for topic in interest_portion:
				user_dict[user_id]['text_interest'].append(topic)
	return user_dict

def interest_judge(user_id):
	filename=directory+user_id+'.json'
	tweet_dict=load_tweet_data(filename)
	featurefile=file1
	MI_dict=load_feature(featurefile)
	count=tweet_class(MI_dict,tweet_dict)
	interest_portion=text_interest_define(count)
	user_dict={}
	if len(interest_portion)!=0:
			user_dict[user_id]={}
			user_dict[user_id]['text_interest']=[]		
			for topic in interest_portion:
				user_dict[user_id]['text_interest'].append(topic)
	else:
		user_dict[user_id]={}
		user_dict[user_id]['text_interest']=[]
	return user_dict,tweet_dict
	
def main():
	'''featurefile=file1
	MI_dict=load_feature(featurefile)
	dir='data/verified_users'
	print dir
	#tweetfile='verified/obama.json'
	#tweet_dict=load_tweet_data(tweetfile)
	#count=tweet_class(MI_dict,tweet_dict)
	#interest_define(count)
	user_dict=analyze_files(dir,MI_dict)
	filename='data/results/userresult2.json'
	f=open(filename,'w')
	f.write(json.dumps(user_dict))'''
	user_id='21625308'
	user_dict=interest_judge(user_id)
	print user_dict
	
if __name__ =='__main__':
	main()
