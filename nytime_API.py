import requests
import json
import sys
import string,re

#target=['Business','Sports','Movies','Technology','Travel']
#target=['Top%2FNews%2FSports%2FSoccer','Top%2FNews%2FSports%2FBaseball','Top%2FNews%2FSports%2FPro%20Basketball','Top%2FNews%2FSports%2FPro%20Football','Top%2FNews%2FEducation']
#target=['Business']
facet='classifiers_facet'
#target=['Top%2FNews%2FU.S.']
#target=['Top%2FNews%2FHealth']
#facet='nytd_section_facet'
#target=['Top%2FFeatures%2FArts%2FMusic']
target=['Top%2FFeatures%2FStyle%2FFashion%20and%20Style']
default_string='politics'
def main():
	for term in target:
		filename=term.lower()+'.json'
		with open(filename,'w') as f:
			for offset in range(0,100):
				print 'offset',offset
				url='http://api.nytimes.com/svc/search/v1/article?format=json&query='+facet+'%3A%5B'+term+'%5D&offset='+str(offset)+'&api-key=0936a86cf1bf6262d7b80da413ff4447:11:67568771'
				r=requests.get(url)
				f.write(json.dumps(r.json()))
				f.write('\n')
		f.close()
		'''g=open(filename,'r')
		for line in g:
			data_decode=json.loads(line.replace('\r','\\r'))
			content_num=len(data_decode['results'])
			#print content_num
			for i in range(0,content_num):
				print data_decode['results'][i]['title']'''
	

if __name__ =='__main__':
	main()