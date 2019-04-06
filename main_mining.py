from pythondb import DataBase
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora
import gensim
import nltk
# nltk.download()
import re
import string
import numpy as np


def classify_doc():
    alltextlist_feb = []
    tv_sitcoms_answertext = DataBase(0, '0', '0', 0, '0', '0', 0).select_answertext()
    for text in tv_sitcoms_answertext: 
        answercount = int(text[1])
        date = str(text[2])
        question = str(text[4])
        # view_weight = int(text[5]) # weight to improve topic mining
        answer = str(text[6])
        # 剩下的事情就是将文本写入文件，然后把数进行清洗，然后进行主题挖掘
        if date.find('2019/1')>=0:
            # alltextlist_feb.append(question) # use append or just use '+' to aggregate string
            if answercount > 0 : alltextlist_feb.append(answer)
            # print(date, question, view_weight, answer)
    # print(alltextlist_feb)
    return alltextlist_feb

def text_clean_set():
    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()
    return stop, exclude, lemma


def text_clean(text):
    stop, exclude, lemma= text_clean_set()
    num_free = re.sub(r'\d+', '', text)
    punc_free = "".join(ch for ch in num_free if ch not in exclude)
    stop_free = " ".join([i for i in punc_free.lower().split() if i not in stop])
    punc_free = "".join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())

    return normalized

def text_clean_run():
    text_cleaned = []
    alltextlist_feb = classify_doc()
    text_cleaned0 = [text_clean(text).split() for text in alltextlist_feb] 
    fw = open('./textfiles/Feb, 2019.txt', 'w')
    for list1 in text_cleaned0:
        for list2 in list1:
            text_cleaned.append(list2)
            if list2 == "": continue
            else:
                list2 = list2 + "\t"
                fw.write(list2)

    # fr = open('./textfiles/Feb, 2019.txt', 'r')
    # print(fr.read())
    # print(text_cleaned0)
    return text_cleaned0

def lda_model():
    text_cleaned0 = text_clean_run()
    dictionary = corpora.Dictionary(text_cleaned0)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_cleaned0]

    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(doc_term_matrix, num_topics=10, id2word = dictionary, passes=50)
    print(ldamodel.print_topics(num_topics=10, num_words=10))




if __name__ == "__main__":
    lda_model()
