# Cleaning Text Steps
# creating a text file and take text from it
# convert all letters into lowercase
# remove punctuation marks

import string
from collections import Counter

import matplotlib.pyplot as plt

import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus') \
        .setSince("2019-05-01") \
        .setUntil("2020-02-29") \
        .setMaxTweets(1000)

    #List of objects gets stored in 'tweets' variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    #Iteration gthrough tweets, storing them temporarily in tweet variable
    #Get text and store it as a list in side 'text_tweets'
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets

text = ""
text_tweets  = get_tweets()
length = len(text_tweets)

for i in range(0,length):
    text = text_tweets[i][0] + " " + text


#text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
# print(string.punctuation)
# print(text)
# print(lower_case)

cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
# print(cleaned_text)
# str.maketrans - str1 - characters to be replaced, str2 - characters with which replaced, str3 - characters to be deleted

tokenized_words = cleaned_text.split()
# print(tokenized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []

for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# print(final_words)

# Use NLP Emotion Algorithm
emotion_list = []

with open('emotion.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n","").replace(",","").replace("'","").strip()
#        print(clear_line)
        word, emotion = clear_line.split(':')
#        print("Word :" + word + " " + "Emotion :" + emotion)

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)

count = Counter(emotion_list)
print(count)


fig , ax1 = plt.subplots()
ax1.bar(count.keys(),count.values())
fig.autofmt_xdate()
#plt.savfig('graph.png')
plt.show()