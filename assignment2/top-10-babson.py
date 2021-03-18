import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import random
import string
import os
print(os.getcwd())


#Top 10 most used words in Babson wikipedia page

def remove_babson():
    
    with open('data/babson.txt','r') as file:
        wellesley_converted_str = file.read()
    return wellesley_converted_str

text = remove_babson()
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]





def process_file_babson():
    hist = {}
    fp = tokens_without_sw

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

bist = process_file_babson()




def most_common(d):
   
    f_w_list = []
    for word, freq in d.items():
        t = (freq, word)
        f_w_list.append(t)

    f_w_list.sort(reverse=True)
    return f_w_list

def print_most_common(d, num=10):

    t = most_common(d)
    for freq, word in t[:num]:
        print(word, "\t", freq)

print(print_most_common(bist))








