import requests
import json
import sys
import string,re,math,random,copy
import unicodedata,os
__author__='wczhang'
from classifier import interest_judge
from news_API import get_news
from screen_name import get_id,get_tweets
import unicodedata

default_dir='data/users/'

def account_to_news(account_string):
	user_id=get_id(account_string)
	get_tweets(account_string,default_dir)
	user_dict,tweet_dict=interest_judge(user_id)
	tweet_string=dict_to_string(tweet_dict)
	interest_list=user_dict[user_id]['text_interest']
	news_list=[]
	if len(interest_list)>0:
		for interest in interest_list:
			#interest=interest_list[0]
			news_temp_list=get_news(interest)
			news_list=news_list+news_temp_list
	else:
		news_list=[]
	#print news_list
	return news_list,interest_list,tweet_string
	
def news_result(news_list):
	result_str= ''
	for news in news_list:
		result_str = result_str + str('Title')+ ':' +str(news['title'].encode('ascii','ignore')) + '\n'
		result_str = result_str + str('Data')+ ':' +str(news['date'].encode('ascii','ignore')) + '\n'
		result_str = result_str + str('Url')+ ':' +str(news['url'].encode('ascii','ignore')) + '\n'
		result_str = result_str + '\n'
	return result_str
	
def interest_result(interest_list):
	result_str= ''
	for interest in interest_list:
		result_str = result_str + str(interest) + ' '
	return result_str
	
	
def dict_to_string(tweet_dict):
	tweet_string=''
	for keys in tweet_dict.keys():
		tweet_string=tweet_string+keys+ ' : ' + tweet_dict[keys]+'\n'
		tweet_string = tweet_string + '\n'
	return tweet_string
	
if __name__ =='__main__':
	account_string='BarackObama'
	news_list,interest_list=account_to_news(account_string)
	print news_result(news_list)
	print interest_list
	