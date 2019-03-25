from pythondb import DataBase
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
# nltk.download()
import re
import string
import numpy as np


def classify_doc():
    questionlist_feb = []
    answerlist_feb = []
    alltextlist_feb = []
    tv_sitcoms_answertext = DataBase(0, '0', '0', 0, '0', '0', 0).select_answertext()
    for text in tv_sitcoms_answertext:
        date = str(text[2])
        question = str(text[4])
        # view_weight = int(text[5]) # weight to improve topic mining
        answer = str(text[6])
        # 剩下的事情就是将文本写入文件，然后把数进行清洗，然后进行主题挖掘
        if date.find('2019/2')>=0:
            questionlist_feb.append(question)
            answerlist_feb.append(answer)
            alltextlist_feb.append(question) # use append or just use '+' to aggregate string
            alltextlist_feb.append(answer)
            # print(date, question, view_weight, answer)
    # print(alltextlist_feb)
    return alltextlist_feb

def text_clean_set():
    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()
    stemmer = PorterStemmer()
    return stop, exclude, lemma, stemmer

def text_clean(text):
    stop, exclude, lemma, stemmer = text_clean_set()
    num_free = re.sub(r'\d+', '', text)
    stop_free = " ".join([i for i in num_free.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    # stem_word = stemmer.stem(punc_free)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())

    return normalized

def text_clean_run():
    alltextlist_feb = classify_doc()
    text_cleaned = [text_clean(text).split() for text in alltextlist_feb] 
    fw = open('./textfiles/Feb, 2019.txt', 'w')
    for list1 in text_cleaned:
        for list2 in list1:
            list2 = list2 + " "
            fw.write(list2)
    # fr = open('./textfiles/Feb, 2019.txt', 'r')
    print(text_cleaned)

if __name__ == "__main__":
    text_clean_run()
