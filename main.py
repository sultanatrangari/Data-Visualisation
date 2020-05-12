# Cleaning Text Steps
# creating a text file and take text from it
# convert all letters into lowercase
# remove punctuation marks

import string
from collections import Counter
from nltk.tokenize  import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
# print(string.punctuation)
# print(text)
# print(lower_case)

cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
# print(cleaned_text)
# str.maketrans - str1 - characters to be replaced, str2 - characters with which replaced, str3 - characters to be deleted

# splitting text into words
tokenized_words = word_tokenize(cleaned_text,"english")
#tokenized_words = cleaned_text.split()
# print(tokenized_words)

#stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
#              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
#              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
#             "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
#             "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
#              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
#              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
#              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
#              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
#              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []

for word in tokenized_words:
    if word not in stopwords.words("english"):
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

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")


sentiment_analyse(cleaned_text)

fig , ax1 = plt.subplots()
ax1.bar(count.keys(),count.values())
fig.autofmt_xdate()
#plt.savfig('graph.png')
plt.show()