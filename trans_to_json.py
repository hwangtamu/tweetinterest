import requests
import json
import sys
import string,re,math,random,copy
import unicodedata
__author__='wczhang'

target=['Travel','Politics','Technology','Sports','Movies','Education','Business']


f=open('lda.txt','r')
topic=0
MI_dict={}
for line in f:
	line=line.replace('\t',' ')
	words=line.split(' ')
	MI_dict[target[topic]]={}
	MI_dict[target[topic]]['totalscore']=0
	i=0
	#print words
	while i<len(words):
		if i>2 and i<len(words)-1:
			#print words[i]
			if words[i+1].find('E')!=-1:
				element=words[i+1].split('E')
				number=float(element[0])*math.pow(10,float(element[1]))
				#print number
			else:
				#print words[i+1]
				number=float(words[i+1])
			MI_dict[target[topic]][words[i]]=number
			MI_dict[target[topic]]['totalscore']=MI_dict[target[topic]]['totalscore']+number
			i=i+2
		else:
			i=i+1
		#print words[i]
	topic=topic+1
filename='featureword/lda.json'
f=open(filename,'w')
f.write(json.dumps(MI_dict))