import csv
import numpy as np
import pandas as pd
import statistics as st
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
stop_words=set(stopwords.words('english'))
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')


from cleaningnew2 import fn_themes
list_themes=fn_themes()
dth = pd.DataFrame(list_themes)

#READING THE DATAFRAME

ff=pd.read_csv('initial_data_set.csv',encoding='utf8')

#URL-STD VALUE

ffu=ff.url
ffun=ffu.fillna("http://www.ted.com")
#print(" ")


#views
ffv=ff.views
ffvn=[]
mini=min(ffv)
maxi=max(ffv)
for i in ffv:
	if(i>mini or i<maxi):
		ffvn.append(i)
	   
mean_data=np.mean(ffvn)
ffvn=ffv.fillna(int(mean_data))


#ID-HOTDECK AND ADDITION

ffid=ff.id
for i in ffid:
	ff['id'] = pd.to_numeric(ff['id'])
	ff['id'].fillna(0,inplace=True)
   
l=list(ffid)
nl=[]
nl=l
fin=[]

   
if(l[0]==0):
	fin.append(0)
	l.remove(l[0])
for i in l:
	if(i==0):
		n=l.index(i)
		x=l[n-1]
		fin.append(x+1)
		l[n]=x+1
	elif(i!=0):
		fin.append(i)

print("")

#TED_EVENT-MODE

ffte=ff.ted_event
mode_data=st.mode(ffte)
fften=ffte.fillna(mode_data)
print(" ")


def foo():
	s=[]
	
	s.append(fin)#id
	s.append(list(fften))#ted_event
	s.append(list(ffun))#url
	s.append(list(ffvn))#views

	return s