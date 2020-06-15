import csv
import pandas as pd
from cleaningnew2 import demo_1
from cleaningnew4 import foo

somelist = demo_1()
f=foo()
print("f:",f )
"""
for i in somelist:
    print(i,"\n")
"""


df=pd.DataFrame(columns=['comments','description','film_date','id', 'published_date', 'related_tags','related_themes','related_videos','speaker','ted_event','title','url','views','transcripts'])	

i=0
#a=[,]
while i<1203:
	if i not in somelist[9] :#or not somelist[2][i][0].isalnum():
		df=df.append({"comments":somelist[0][i],"description":somelist[1][i],"published_date":somelist[3][i],'film_date':somelist[2][i],'id':f[0][i],'related_tags':somelist[4][i],'related_themes':somelist[5][i],'related_videos':somelist[6][i],'speaker':somelist[7][i],'ted_event':f[1][i],'title':somelist[8][i],'url':f[2][i],'views':f[3][i],'transcripts':somelist[10][i]},ignore_index=True)
	i+=1


#print(df.head())
df.to_csv('output_final.csv')





