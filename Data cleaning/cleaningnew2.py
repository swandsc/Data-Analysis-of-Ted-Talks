#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
stop_words=set(stopwords.words('english'))
import numpy as np

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("talks_uncleaned_2.csv") 
data2 = pd.read_csv("talks.csv") 
# Preview the first 5 lines of the loaded data 
data.head()
#data.tail()


# In[9]:


'''
l=list(data.comments)
#print(l)
#new_comments=(list(data.comments.fillna(data.comments.mean())))
'''


# In[10]:

transcripts=list(data2.transcript)

mean=data.comments.mean()
mean=int(mean)
new_comments=list(data.comments.fillna(mean))
#print(new_comments)


# In[11]:


new_publish_date=list(data.publish_date.fillna(method='ffill'))

new_film_date=list(data.film_date.fillna(method='ffill'))
#print(len(new_film_date))

#print(new_publish_date)
#new_description=list(data.description.fillna((data.related_themes)[data.sl_no][0]))
#for i in new_publish_date:
 #   #print(i,"\n")


# In[12]:


#Replace tags by tags of the same speaker
#Otherwise replace them by words in themes(after removing stopwords)

list_dont_care=[]

data.related_tags.fillna(",",inplace=True)
data.speaker.fillna(",",inplace=True)
##print(data.related_tags)
org_rel_tags=list(data.related_tags)
org_rel_themes=list(data.related_themes)
org_speaker=list(data.speaker)
##print(org_speaker)
new_rel_tags=[]
##print(org_rel_themes)
count=-1
for i in org_rel_tags:
	count+=1
	temp=i
	##print("i ",i,"\n")
	if (i==","):
		##print("i ",i)
		ind_tag=count
		##print("ind_tag: ",ind_tag)
		speaker=org_speaker[ind_tag]
		##print("org_speaker ",speaker)
		if speaker !=",":
			indices = [i for i, x in enumerate(org_speaker) if x == speaker]
			#print(indices)
			if indices[0]!=ind_tag:
				#print("in indices 1")
				#print(indices[0])
				temp=list(org_rel_tags[indices[0]].split())
			elif len(indices)>1:
				#print("in indices 2")
				#print(indices[1])
				temp=list(org_rel_tags[indices[1]].split())
			else: 
				try:
					#print("in else")

					filtered_sentence = []
					##print(org_rel_themes)
					##print(list(org_rel_themes))
					##print(list(org_rel_themes.index(1)))
					themes=org_rel_themes[count]
					##print("themes ",themes)
					##print(org_rel_themes[org_rel_tags.index(i)])
					word_tokens =tokenizer.tokenize(themes)
					#word_tokens = word_tokenize(themes) 
					##print(word_tokens)
					for w in word_tokens: 
						if (w not in stop_words) and len(w)>3: 
							filtered_sentence.append(w)
					#print("Filtered sent: ",filtered_sentence)
					temp=filtered_sentence 
				##print("temp ",temp,"\n################################################\n")
				#new_rel_tags.append(filtered_sentence)
				except:
					list_dont_care.append(count)

		else: 
			try:
				#print("in else")

				filtered_sentence = []
				##print(org_rel_themes)
				##print(list(org_rel_themes))
				##print(list(org_rel_themes.index(1)))
				themes=org_rel_themes[count]
				##print("themes ",themes)
				##print(org_rel_themes[org_rel_tags.index(i)])
				word_tokens =tokenizer.tokenize(themes)
				#word_tokens = word_tokenize(themes) 
				##print(word_tokens)
				for w in word_tokens: 
					if (w not in stop_words) and len(w)>3: 
						filtered_sentence.append(w)
				#print("Filtered sent: ",filtered_sentence)
				temp=filtered_sentence 
				#new_rel_tags.append(filtered_sentence)
			except:
				list_dont_care.append(count)
	#print("temp ",temp,"\n################################################\n")

	new_rel_tags.append(temp)

#print("list_dont_care  \n",list_dont_care)

# In[18]:


#Replacing missing themes with a part of the title
data.related_themes.fillna(",",inplace=True)
data.title.fillna(",",inplace=True)
org_title=list(data.title)
org_rel_themes=list(data.related_themes)
org_speaker=list(data.speaker)
new_rel_themes=[]
count=-1
for i in org_rel_themes:
	count+=1
	temp=i
	if i==",":
		speaker=org_speaker[count]
		if speaker!=",":
			temp=org_title[count][len(speaker):]
		else:
			a=" ".join((org_title[count]).split(" ", 2)[2:])
			tokenizer.tokenize(a)
			#print("a: ",a)
			temp=a
		temp=[k for k in temp.split() if k.isalnum() ]
		l=[]
		s=""
		for i in temp:
			##print("i ",i)
			s=s+i+" "
		#print("s is",s)
		temp=s
		if not s:
			list_dont_care.append(count)
	#print("temp : ",temp)
		#print(count)
	temp=temp.replace("]",'')
	temp=temp.replace("[",'')
	temp=temp.replace("'",'')

	#print(type(temp))	
	new_rel_themes.append(temp)
'''
for i in (new_rel_themes):
	print(i,"\n####################################\n")
'''
#print("list_dont_care: ",list_dont_care)


# In[17]: DESCRIPTION
(data.description.fillna(",",inplace=True))
org_des=list(data.description)
new_des=[]
count=-1
for i in org_des:
	count+=1
	if i==",":
		#print(count,"This is imp%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",new_rel_themes[count],type(new_rel_themes[count]))
		i=new_rel_themes[count]

	new_des.append(i)
'''
for j in new_des:
	print(j,"#######################################\n")
'''


#speaker
new_speaker=[]
count=-1
for i in org_speaker:
	count+=1
	if i==",":
		if ":" in org_title[count]:

			i=org_title[count].split(":")[0]
		elif "-" in org_title[count]:

			i=org_title[count].split("-")[0]
		else:
			try:
				
				i="".join(org_title[count].split()[0]+" "+org_title[count].split()[1])
			except:
				i="unknown"
				list_dont_care.append(count)
	#print(i,"\n########################\n")
	new_speaker.append(i)
'''
for j in new_speaker:
	print(j,"#######################################\n")
'''

#TITLE(speaker+themes)
new_title=[]
count=-1
for i in org_title:
	count+=1
	if i==",":
		#print("in if")
		i="".join(new_speaker[count]+":"+new_rel_themes[count].split(",")[0])
	#print(count,i)
	new_title.append(i)


#RELATED VIDEOS
data.related_videos.fillna(",",inplace=True)
org_rel_vid=list(data.related_videos)
new_rel_vid=[]
count=-1
for i in org_rel_vid:
	count+=1
	if i==",":
		i="["+new_speaker[count]+":"+"Ted talks"+"]"
	new_rel_vid.append(i)
for j in new_rel_vid:
	print(j,"\n")


def demo_1():
	somelist=[]
	somelist.append(new_comments)
	somelist.append(new_des)
	somelist.append(new_film_date)
	somelist.append(new_publish_date)
	somelist.append(new_rel_tags)
	somelist.append(new_rel_themes)
	somelist.append(new_rel_vid)
	somelist.append(new_speaker)
	somelist.append(new_title)
	somelist.append(list_dont_care)
	somelist.append(transcripts)
	return somelist


def fn_themes():
	return new_rel_tags




