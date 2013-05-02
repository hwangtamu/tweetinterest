import requests
import json
import sys
import string,re,math,random,copy
import unicodedata
__author__='wczhang'

target=['Business','Sports','Movies','Technology','Travel','Education','Politics','Fashion','Music','Science','Health']
feature_number=10
cate_number=11
total_doc_num=11000
cate_doc_num=1000
# note that category of politics is different from others, because of its structure in json file
default_cate='Politics'
default_string='politics'

data_dir='data/rawdata/'

def deal_exception_letter(text):
	replace_text=re.findall(r"&#x\w+;",text)
	new_text=[]
	new_text.append(text)
	for term in replace_text:
		temp_text=new_text[-1].replace(term,' ')
		new_text.append(temp_text)
	data=re.findall(r"[A-Za-z']+",new_text[-1])
	return data

def data_extraction(stop_dict):
	cate_id=0 #category number
	doc_id=0 #document id 
	feature_dict={} # word and its document
	doc_cate_dict={} # document corresponding to category
	full=0
	for term in target:
		filename=data_dir+term.lower()+'.json'
		#write_filename=term.lower()+'.txt'
		f=open(filename,'r')
		#g=open(write_filename,'w')
		count_for_politics=0
		for line in f:
			#if politics is full
			if target[cate_id]==default_cate:
				if count_for_politics==1000:
					break
			
			data_decode=json.loads(line.replace('\r','\\r'))
			content_num=len(data_decode['results'])
			
			for i in range(0,content_num):
				# if it does not contain politics
				if target[cate_id]==default_cate:
					if data_decode['results'][i]['url'].find(default_string)==-1:
						continue
				#if politics is full
				if count_for_politics==1000:
					break
				
				# extract data from title and body
				data_title=deal_exception_letter(data_decode['results'][i]['title'])
				if data_decode['results'][i].get('body')!=None:
					data_body=deal_exception_letter(data_decode['results'][i]['body'])
				else:
					data_body=[]
				data_title.extend(data_body)
				for word in data_title:
					word=word.lower()

					if stop_dict.get(word)!=None:
						continue
					
					if feature_dict.get(word)==None:
						feature_dict[word]={}
						feature_dict[word][doc_id]=1
					else:
						feature_dict[word][doc_id]=1
						
				doc_cate_dict[doc_id]=cate_id
				doc_id=doc_id+1
				if target[cate_id]==default_cate:
					count_for_politics=count_for_politics+1
		cate_id=cate_id+1
	print 'category number :',cate_id,' document number: ',doc_id	
	return (feature_dict,doc_cate_dict)

def feature_selection(feature_dict,doc_cate_dict):
	#info_gain: info_gain[topic][word]=mutual_information_score
	#MI_dict: MI_dict[topic][word]=mutual_information_score,but it only has feature_number words in one topic
	info_gain={}
	for i in range(0,cate_number):
		info_gain[target[i]]={}
	info_gain=cal_mutual_info(feature_dict,doc_cate_dict,info_gain)
	MI_dict={}
	for i in range(0,cate_number):
		print "category: ",target[i]
		MI_dict[target[i]]={}
		MI_dict[target[i]]['totalscore']=0
		j=0
		for keys,values in sorted(info_gain[target[i]].items(),reverse=True,key=myFN):
			if j>feature_number:
				break
			print keys,values
			MI_dict[target[i]][keys]=values
			MI_dict[target[i]]['totalscore']=MI_dict[target[i]]['totalscore']+values
			j=j+1
	return (MI_dict,info_gain)

def cal_mutual_info(feature_dict,doc_cate_dict,info_gain):
	for word in feature_dict.keys():
		for i in range(0,cate_number):
			N_11=0
			N_10=0
			N_01=0
			N_00=0
			N=total_doc_num
			for doc_id in feature_dict[word].keys():
				if doc_cate_dict[doc_id]==i:
					N_11=N_11+1
				else:
					N_10=N_10+1
			N_01=cate_doc_num-N_11
			N_00=total_doc_num-N_10-N_11-N_01
			MI=0
			if N_11!=0:
				MI=MI+N_11*math.log((N*N_11/float((N_11+N_10)*(N_11+N_01))),2)/float(N)
			if N_10!=0:
				MI=MI+N_10*math.log(N*N_10/float((N_11+N_10)*(N_10+N_00)),2)/float(N)
			if N_01!=0:
				MI=MI+N_01*math.log(N*N_01/float((N_00+N_01)*(N_11+N_01)),2)/float(N)
			if N_00!=0:
				MI=MI+N_00*math.log(N*N_00/float((N_00+N_01)*(N_10+N_00)),2)/float(N)
			info_gain[target[i]][word]=MI
	return info_gain

def myFN(s):
	return s[-1]	
	
def load_stop_word(filename):
	stop_dict={}
	f=open(filename,'r')
	for line in f:
		word=re.findall(r"[\w']+",line,flags=re.UNICODE)
		stop_dict[word[0]]=1
	f.close()
	return stop_dict

def main():
	stop_filename='stopword.txt'
	stop_dict=load_stop_word(stop_filename)
	feature_dict,doc_cate_dict=data_extraction(stop_dict)
	MI_dict,info_gain=feature_selection(feature_dict,doc_cate_dict)
	
	'''filename='data/featureword/featureresults.json'
	f=open(filename,'w')
	f.write(json.dumps(MI_dict))
	'''
	
	
if __name__ =='__main__':
	main()