import random
import string
import os
print(os.getcwd())
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')


def process_file_babson(filename):
    
    hist = {}
    fp = open(filename, encoding='UTF8')

  

    strippables = string.punctuation + string.whitespace

    for line in fp:
        
        if line.startswith('*** END OF THIS PROJECT'):
            break
        

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist




bist = process_file_babson('data/babson.txt')
print(bist) 
# Bist is == to the name for the babson dictionary, where the key is the unique word used, and value is the frequency of the key


def process_file_wellesley(filename):
    
    hist = {}
    fp = open(filename, encoding='UTF8')

  

    strippables = string.punctuation + string.whitespace

    for line in fp:
        
        if line.startswith('*** END OF THIS PROJECT'):
            break
        

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist




wist = process_file_wellesley('data/wellesley.txt')
print(wist) 
# Wist is == to the name for the wellesley dictionary, where the key is the unique word used, and value is the frequency of the key

# Characterize words by frequency

"""
For words in babson wiki page
"""
def babo_word(word):
    print(bist[word])

babo_word("wellesley")
"""
For words in wellesley wiki page
"""

def wellesley_word(word):
    print(wist[word])

wellesley_word("babson")

"""
After characterizing text words by their frequencies, we can see that the word wellesley appears in the babson
wikipiedia page 3 times. It is interesting to note that the word babson also appears 3 times in the wellesley wikipedia page.
"""

#Doing natural language processing

def babo():
    
    with open('data/babson.txt','r') as file:
        babson_converted_str = file.read()
    return babson_converted_str



def sentiment_babson():
    
    sentence_babo = babo()

    sentence = sentence_babo
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    print(score)
    

sentiment_babson()

# def wells():
    
#     with open('data/wellesley.txt','r') as file:
#         wellesley_converted_str = file.read()
#     return wellesley_converted_str

# def sentiment_wellesley():
    
#     sentence_wells = wells()

#     sentence = sentence_wells
#     score = SentimentIntensityAnalyzer().polarity_scores(sentence)
#     print(score)

# sentiment_wellesley()

#Sentiment Analysis for Wellesley did not work for whatever reason

# Computing summary statistics

"""
What words appear in Babson's wikipedia page which do not appear in Wellesley College wikipedia page?
And vice versa?
"""
#To find which words appear in Babson's and not Wellesleys
def subtract_wellesley(d1, d2):
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

babson_not_in_wellesley = subtract_wellesley(bist, wist)


def final_output_babson():
    res = []
    for k in babson_not_in_wellesley.keys():
        res.append(k)
    res.sort()
    return res

print(final_output_babson())

print()
print()
print()

#To find which appear in Wellesleys, and not Babsons wikipedia pages
def subtract_babson(d1, d2):
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

wellesley_not_in_babson = subtract_babson(wist, bist)


def final_output_wellesley():
    res = []
    for k in wellesley_not_in_babson.keys():
        res.append(k)
    res.sort()
    return res

print(final_output_wellesley())

print()
print()

