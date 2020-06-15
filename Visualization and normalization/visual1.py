        # -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:23:12 2019

@author: swanuja
"""
#Import modules
import pandas as pd
import csv 
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
#from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from wordcloud import WordCloud
import matplotlib.pyplot
import pylab
import seaborn as sns


#Reading the CSV file
df = pd.read_csv(r'output_final.csv',encoding='latin-1')

#Making a list of all the columns
list_views_max = list(df.views) #items get removed from here
list_views = list(df.views)
list_title = list(df.title)
list_comments = list(df.comments)
list_comments_max = list(df.comments) #items get removed from here
list_tags = list(df.related_tags)
list_events = list(df.ted_event)
list_transcripts = list(df.transcripts)
list_speakers = list(df.speaker)

#sns.distplot(df['views'])

plt.rcParams["figure.figsize"]=(10,5)

#MODE OF TED TALK EVENTS
print("THE EVENT THAT HAD THE MAXIMUM NUMBER OF TALKS IS :" )
print(df.ted_event.mode())

#MODE OF SPEAKERS
print("THE SPEAKER WHO HAS GIVEN THE MOST TALKS, WITH 9 TED TALKS :" )
print(df.speaker.mode())


#BAR GRAPH TO FIND TOP N VIEWS AND TITLES

#function to sort and find top N elements and then print the graph (within the same function)
def Nmaxviews(list1, N): 
    final_list = [] 
    max_title_list = []
  
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        max_title_list.append(list_title[list_views_max.index(max1)])
        list1.remove(max1); 
        final_list.append(max1)

    #print(final_list)
    #print(max_title_list)

    #plotting the bar graph
    index = np.arange(len(max_title_list))
    plt.bar(index, final_list)
    plt.xlabel('Title', fontsize=20)
    plt.ylabel('Views', fontsize=20)
    plt.xticks(index, max_title_list, fontsize=10, rotation=90)
    plt.title('Top 10 most viewed videos on TedTalks')
    plt.show()

Nmaxviews(list_views_max, 10)

#BAR GRAPH TO FIND VIDEOS MOST COMMENTED ON

#function to sort and find top N elements and then print the graph (within the same function)
def Nmaxviews(list1, N): 
    final_list = [] 
    max_title_list = []
  
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        max_title_list.append(list_title[list_comments_max.index(max1)])
        list1.remove(max1); 
        final_list.append(max1)
        
    #print(final_list)
    #print(max_title_list)
    
    #plotting the bar graph
    index = np.arange(len(max_title_list))
    plt.bar(index, final_list)
    plt.xlabel('Title', fontsize=20)
    plt.ylabel('No. of comments', fontsize=20)
    plt.xticks(index, max_title_list, fontsize=10, rotation=90)
    plt.title('Top 10 most commented on videos on TedTalks')
    plt.show()
    
Nmaxviews(list_comments_max, 10)



# CODE TO GET A SET OF THE TAGS

#this line removes the first and ending opening and closing brackets
for i in range(len(df.related_tags)):
    df.related_tags[i] = df.related_tags[i][1:len(df.related_tags[i])-1:]
    
#these lines initializes all the lists to None
related_tags_new = [None] * len(df.related_tags)
related_tags_new1 = [None] * len(df.related_tags)
related_tags_new2 = [None] * len(df.related_tags)
related_tags_new3 = [None] * len(df.related_tags)
related_tags_ult = [None] * len(df.related_tags)


#this removes all the unnecessary quotes and brackets
for i in range(len(df.related_tags)):
        related_tags_new[i]=(df.related_tags[i]).replace("'","")
        related_tags_new1[i]=(related_tags_new[i]).replace('"',"")
        related_tags_new2[i]=(related_tags_new1[i]).replace("]","")
        related_tags_new3[i]=(related_tags_new2[i]).replace("[","")
        
#this splits the words by commas
for i in range(len(related_tags_new)):
    related_tags_ult[i]=related_tags_new3[i].split(", ")

#this makes a set of the tags
related_tags_set = set()
tags_wordcloud = []
for i in range(len(related_tags_ult)):
    for j in range(len(related_tags_ult[i])):
        related_tags_set.add(related_tags_ult[i][j])
        tags_wordcloud.append(related_tags_ult[i][j])
        
#print(tags_wordcloud)

#wordcloud of tags
        
unique_string=(" ").join(tags_wordcloud)
wordcloud = WordCloud(width = 1500, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()
        
#print(related_tags_ult)
print('\n\n')

#print("THE SET OF TAGS ARE :")
#print(related_tags_set)

tags_count_dict={}
for i in range(len(related_tags_ult)):
    for j in range(len(related_tags_ult[i])):
        #if((related_tags_ult[i][j]) in tags_dict_set):
        tags_count_dict[related_tags_ult[i][j]]=tags_count_dict.get(related_tags_ult[i][j],0)+1
    
#print(tags_count_dict)

D = tags_count_dict

#print(D)

list_values = []
list_values=list(D.values())
list_values.sort(reverse=True)

top_ten_values = []

for i in range(15):
    top_ten_values.append(list_values[i])
    
#print(top_ten_values)
#print(list_values)

list_keys = []
list_keys=list(D.keys())

#print(list_keys)

'''
another_list_keys = []
for i in list_values:
    print(list_keys[list_values.index(i)])
    #another_list_keys.append(list_keys[list_values.index(i)])
    
#print(another_list_values)
    
top_ten_keys = []
for i in range(15):
    top_ten_keys.append(another_list_keys[i])
    
#print(top_ten_keys)
    
for i in top_ten_values:
    for key, value in D:
        if value==i:
            print(key)

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(top_ten_keys))
    plt.bar(top_ten_keys, top_ten_values)
    plt.xlabel('Tag', fontsize=20)
    plt.ylabel('Count', fontsize=20)
    plt.xticks(index, top_ten_keys, fontsize=10, rotation=30)
    plt.title('Top 15 most used tags')
    plt.show()
    
plot_bar_x()

tags_views_dict={}
for i in range(len(related_tags_ult)):
    for j in range(len(related_tags_ult[i])):
        #if((related_tags_ult[i][j]) in tags_dict_set):
        tags_views_dict[related_tags_ult[i][j]]=tags_views_dict.get(related_tags_ult[i][j],0)+(list_views[i])
        
DD = tags_views_dict

#print(D)

list_values_views = []
list_values_views=list(DD.values())
list_values_views.sort(reverse=True)

top_ten_values_views = []

for i in range(15):
    top_ten_values_views.append(list_values_views[i])
#print(top_ten_values_views)
#print(list_values)

list_keys_views = []
list_keys_views=list(DD.keys())

another_list_keys_views = []
for i in list_values_views:
    #print(list_keys[list_values.index(i)])
    another_list_keys_views.append(list_keys_views[list_values_views.index(i)])
    
#print(another_list_values)
    
top_ten_keys_views = []
for i in range(15):
    top_ten_keys_views.append(another_list_keys_views[i])
    
#print(top_ten_keys_views)


def plot_bar_x_views():
    # this is for plotting purpose
    index = np.arange(len(top_ten_keys_views))
    plt.bar(top_ten_keys_views, top_ten_values_views)
    plt.xlabel('Tag', fontsize=20)
    plt.ylabel('No of views', fontsize=20)
    plt.xticks(index, top_ten_keys_views, fontsize=10, rotation=30)
    plt.title('Which tags have the most views')
    plt.show()
    
plot_bar_x_views()
        
#print(tags_views_dict)

tags_comments_dict={}
for i in range(len(related_tags_ult)):
    for j in range(len(related_tags_ult[i])):
        #if((related_tags_ult[i][j]) in tags_dict_set):
        tags_comments_dict[related_tags_ult[i][j]]=tags_comments_dict.get(related_tags_ult[i][j],0)+(list_comments[i])
        
#print(tags_comments_dict)
'''

#WORKING WITH TRANSCRIPTS
list_transcripts_words=[None] * len(list_transcripts)
list_transcripts1=[None] * len(list_transcripts)
list_transcripts2=[None] * len(list_transcripts)
list_transcripts3=[None] * len(list_transcripts)
list_transcripts4=[None] * len(list_transcripts)
list_transcripts5=[None] * len(list_transcripts)
list_transcripts6=[None] * len(list_transcripts)


for i in range(len(list_transcripts)):
    list_transcripts1[i]=(list_transcripts[i]).replace(',',"")
    list_transcripts2[i]=(list_transcripts1[i]).replace('.',"")
    list_transcripts3[i]=(list_transcripts2[i]).replace('?',"")
    list_transcripts4[i]=(list_transcripts3[i]).replace('/',"")
    list_transcripts5[i]=(list_transcripts4[i]).replace('(',"")
    list_transcripts6[i]=(list_transcripts5[i]).replace(')',"")
    
    
for i in range(len(list_transcripts6)):
    list_transcripts_words[i]=list_transcripts6[i].split(" ")
    
for i in range(len(list_transcripts_words)):
    for j in range(len(list_transcripts_words[i])):
        list_transcripts_words[i][j]=list_transcripts_words[i][j].lower()
    
#print(list_transcripts_words)

#List to get the number of words per transcript
no_of_words=[None] * len(list_transcripts_words)
for i in range(len(list_transcripts_words)):
    no_of_words[i]=len(list_transcripts_words[i])

#print(no_of_words)

#stop_words=set(stopwords.words("english"))
#print(stop_words)

#Scatter plot to show length of video (no of words) vs no of views
matplotlib.pyplot.scatter(no_of_words,list_views)
matplotlib.pyplot.show()

#Cleaning of transcript to get a wordcloud  
stop_words=["a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", "and", "any", "are", "aren", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can", "couldn", "couldn't", "d", "did", "didn", "didn't", "do", "does", "doesn", "doesn't", "doing", "don", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn", "hadn't", "has", "hasn", "hasn't", "have", "haven", "haven't", "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "isn", "isn't", "it", "it's", "its", "itself", "just", "ll", "m", "ma", "me", "mightn", "mightn't", "more", "most", "mustn", "mustn't", "my", "myself", "needn", "needn't", "no", "nor", "not", "now", "o", "of", "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "re", "s", "same", "shan", "shan't", "she", "she's", "should", "should've", "shouldn", "shouldn't", "so", "some", "such", "t", "than", "that", "that'll", "the", "their", "theirs", "them", "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until", "up", "ve", "very", "was", "wasn", "wasn't", "we", "were", "weren", "weren't", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "won", "won't", "wouldn", "wouldn't", "y", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "could", "he'd", "he'll", "he's", "here's", "how's", "i'd", "i'll", "i'm", "i've", "let's", "ought", "she'd", "she'll", "that's", "there's", "they'd", "they'll", "they're", "they've", "we'd", "we'll", "we're", "we've", "what's", "when's", "where's", "who's", "why's", "would", "able", "abst", "accordance", "according", "accordingly", "across", "act", "actually", "added", "adj", "affected", "affecting", "affects", "afterwards", "ah", "almost", "alone", "along", "already", "also", "although", "always", "among", "amongst", "announce", "another", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "apparently", "approximately", "arent", "arise", "around", "aside", "ask", "asking", "auth", "available", "away", "awfully", "b", "back", "became", "become", "becomes", "becoming", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "believe", "beside", "besides", "beyond", "biol", "brief", "briefly", "c", "ca", "came", "cannot", "can't", "cause", "causes", "certain", "certainly", "co", "com", "come", "comes", "contain", "containing", "contains", "couldnt", "date", "different", "done", "downwards", "due", "e", "ed", "edu", "effect", "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending", "enough", "especially", "et", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "except", "f", "far", "ff", "fifth", "first", "five", "fix", "followed", "following", "follows", "former", "formerly", "forth", "found", "four", "furthermore", "g", "gave", "get", "gets", "getting", "give", "given", "gives", "giving", "go", "goes", "gone", "got", "gotten", "h", "happens", "hardly", "hed", "hence", "hereafter", "hereby", "herein", "heres", "hereupon", "hes", "hi", "hid", "hither", "home", "howbeit", "however", "hundred", "id", "ie", "im", "immediate", "immediately", "importance", "important", "inc", "indeed", "index", "information", "instead", "invention", "inward", "itd", "it'll", "j", "k", "keep", "keeps", "kept", "kg", "km", "know", "known", "knows", "l", "largely", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "lets", "like", "liked", "likely", "line", "little", "'ll", "look", "looking", "looks", "ltd", "made", "mainly", "make", "makes", "many", "may", "maybe", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "million", "miss", "ml", "moreover", "mostly", "mr", "mrs", "much", "mug", "must", "n", "na", "name", "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need", "needs", "neither", "never", "nevertheless", "new", "next", "nine", "ninety", "nobody", "non", "none", "nonetheless", "noone", "normally", "nos", "noted", "nothing", "nowhere", "obtain", "obtained", "obviously", "often", "oh", "ok", "okay", "old", "omitted", "one", "ones", "onto", "ord", "others", "otherwise", "outside", "overall", "owing", "p", "page", "pages", "part", "particular", "particularly", "past", "per", "perhaps", "placed", "please", "plus", "poorly", "possible", "possibly", "potentially", "pp", "predominantly", "present", "previously", "primarily", "probably", "promptly", "proud", "provides", "put", "q", "que", "quickly", "quite", "qv", "r", "ran", "rather", "rd", "readily", "really", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "respectively", "resulted", "resulting", "results", "right", "run", "said", "saw", "say", "saying", "says", "sec", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sent", "seven", "several", "shall", "shed", "shes", "show", "showed", "shown", "showns", "shows", "significant", "significantly", "similar", "similarly", "since", "six", "slightly", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specifically", "specified", "specify", "specifying", "still", "stop", "strongly", "sub", "substantially", "successfully", "sufficiently", "suggest", "sup", "sure", "take", "taken", "taking", "tell", "tends", "th", "thank", "thanks", "thanx", "thats", "that've", "thence", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "thereto", "thereupon", "there've", "theyd", "theyre", "think", "thou", "though", "thoughh", "thousand", "throug", "throughout", "thru", "thus", "til", "tip", "together", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "ts", "twice", "two", "u", "un", "unfortunately", "unless", "unlike", "unlikely", "unto", "upon", "ups", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "v", "value", "various", "'ve", "via", "viz", "vol", "vols", "vs", "w", "want", "wants", "wasnt", "way", "wed", "welcome", "went", "werent", "whatever", "what'll", "whats", "whence", "whenever", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "whim", "whither", "whod", "whoever", "whole", "who'll", "whomever", "whos", "whose", "widely", "willing", "wish", "within", "without", "wont", "words", "world", "wouldnt", "www", "x", "yes", "yet", "youd", "youre", "z", "zero", "a's", "ain't", "allow", "allows", "apart", "appear", "appreciate", "appropriate", "associated", "best", "better", "c'mon", "c's", "cant", "changes", "clearly", "concerning", "consequently", "consider", "considering", "corresponding", "course", "currently", "definitely", "described", "despite", "entirely", "exactly", "example", "going", "greetings", "hello", "help", "hopefully", "ignored", "inasmuch", "indicate", "indicated", "indicates", "inner", "insofar", "it'd", "keep", "keeps", "novel", "presumably", "reasonably", "second", "secondly", "sensible", "serious", "seriously", "sure", "t's", "third", "thorough", "thoroughly", "three", "well", "wonder", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "co", "op", "research-articl", "pagecount", "cit", "ibid", "les", "le", "au", "que", "est", "pas", "vol", "el", "los", "pp", "u201d", "well-b", "http", "volumtype", "par", "0o", "0s", "3a", "3b", "3d", "6b", "6o", "a1", "a2", "a3", "a4", "ab", "ac", "ad", "ae", "af", "ag", "aj", "al", "an", "ao", "ap", "ar", "av", "aw", "ax", "ay", "az", "b1", "b2", "b3", "ba", "bc", "bd", "be", "bi", "bj", "bk", "bl", "bn", "bp", "br", "bs", "bt", "bu", "bx", "c1", "c2", "c3", "cc", "cd", "ce", "cf", "cg", "ch", "ci", "cj", "cl", "cm", "cn", "cp", "cq", "cr", "cs", "ct", "cu", "cv", "cx", "cy", "cz", "d2", "da", "dc", "dd", "de", "df", "di", "dj", "dk", "dl", "do", "dp", "dr", "ds", "dt", "du", "dx", "dy", "e2", "e3", "ea", "ec", "ed", "ee", "ef", "ei", "ej", "el", "em", "en", "eo", "ep", "eq", "er", "es", "et", "eu", "ev", "ex", "ey", "f2", "fa", "fc", "ff", "fi", "fj", "fl", "fn", "fo", "fr", "fs", "ft", "fu", "fy", "ga", "ge", "gi", "gj", "gl", "go", "gr", "gs", "gy", "h2", "h3", "hh", "hi", "hj", "ho", "hr", "hs", "hu", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ic", "ie", "ig", "ih", "ii", "ij", "il", "in", "io", "ip", "iq", "ir", "iv", "ix", "iy", "iz", "jj", "jr", "js", "jt", "ju", "ke", "kg", "kj", "km", "ko", "l2", "la", "lb", "lc", "lf", "lj", "ln", "lo", "lr", "ls", "lt", "m2", "ml", "mn", "mo", "ms", "mt", "mu", "n2", "nc", "nd", "ne", "ng", "ni", "nj", "nl", "nn", "nr", "ns", "nt", "ny", "oa", "ob", "oc", "od", "of", "og", "oi", "oj", "ol", "om", "on", "oo", "oq", "or", "os", "ot", "ou", "ow", "ox", "oz", "p1", "p2", "p3", "pc", "pd", "pe", "pf", "ph", "pi", "pj", "pk", "pl", "pm", "pn", "po", "pq", "pr", "ps", "pt", "pu", "py", "qj", "qu", "r2", "ra", "rc", "rd", "rf", "rh", "ri", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "rv", "ry", "s2", "sa", "sc", "sd", "se", "sf", "si", "sj", "sl", "sm", "sn", "sp", "sq", "sr", "ss", "st", "sy", "sz", "t1", "t2", "t3", "tb", "tc", "td", "te", "tf", "th", "ti", "tj", "tl", "tm", "tn", "tp", "tq", "tr", "ts", "tt", "tv", "tx", "ue", "ui", "uj", "uk", "um", "un", "uo", "ur", "ut", "va", "wa", "vd", "wi", "vj", "vo", "wo", "vq", "vt", "vu", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y2", "yj", "yl", "yr", "ys", "yt", "zi", "zz","(laughter)","(applause)","-","--"," ","â€œ", "  ", "   ", "â\x80\x94", "â", "â[]<<", "applause", "laughter"]

filtered_sent=[]
for i in range(len(list_transcripts_words)):
    for j in range(len(list_transcripts_words[i])):
        if (list_transcripts_words[i][j]) not in stop_words:
            filtered_sent.append((list_transcripts_words[i][j]))
#print("Tokenized Sentence:",list_transcripts_words)
print('\n\n\n')
#print("Filterd Sentence:",filtered_sent)

ps = PorterStemmer()

stemmed_words=[]
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))

#print("Filtered Sentence:",filtered_sent)
#print("Stemmed Sentence:",stemmed_words)

for i in stemmed_words:
    if(not(i.isalpha())):
        stemmed_words.remove(i)

lem = WordNetLemmatizer()

lem_words=[]
for w in filtered_sent:
    lem_words.append(lem.lemmatize(w))

fdist = FreqDist(lem_words)
fdist.plot(30,cumulative=False)
plt.show()

unique_string=(" ").join(lem_words)
wordcloud = WordCloud(width = 1500, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()
