import requests
import json
import sys
import string,re

topic_dict={
'Business':{'target':'Business','facet':'nytd_section_facet'},
'Sports':{'target':'Sports','facet':'nytd_section_facet'},
'Movies':{'target':'Movies','facet':'nytd_section_facet'},
'Technology':{'target':'Technology','facet':'nytd_section_facet'},
'Travel':{'target':'Travel','facet':'nytd_section_facet'},
'Education':{'target':'Top%2FNews%2FEducation','facet':'classifiers_facet'},
'Politics':{'target':'Top%2FNews%2FU.S.','facet':'classifiers_facet'},
'Health':{'target':'Top%2FNews%2FHealth','facet':'classifiers_facet'},
'Music':{'target':'Top%2FFeatures%2FArts%2FMusic','facet':'classifiers_facet'},
'Fashion':{'target':'Top%2FFeatures%2FStyle%2FFashion%20and%20Style','facet':'classifiers_facet'},
'Science':{'target':'Top%2FNews%2FScience','facet':'classifiers_facet'}
}

interest='Business'

def get_news(interest):
	term=topic_dict[interest]['target']
	facet=topic_dict[interest]['facet']
	offset=0
	url='http://api.nytimes.com/svc/search/v1/article?format=json&query='+facet+'%3A%5B'+term+'%5D&offset='+str(offset)+'&api-key=0936a86cf1bf6262d7b80da413ff4447:11:67568771'
	r=requests.get(url)
	temp_news_dict=r.json()
	news_dict={}
	result_list=temp_news_dict['results']
	#print result_list
	return result_list

if __name__ =='__main__':
	get_news(interest)
