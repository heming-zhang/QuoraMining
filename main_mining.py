from pythondb import DataBase
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora, models
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from biterm.btm import oBTM
from sklearn.feature_extraction.text import CountVectorizer
from biterm.utility import vec_to_biterms, topic_summuary
import pyLDAvis
import spacy
import datetime
import gensim
import nltk
import collections
import re
import string
import numpy as np


def classify_doc():
    alltextlist = []
    tv_sitcoms_answertext = DataBase(0, '0', '0', 0, '0', '0', 0).select_answertext()
    for text in tv_sitcoms_answertext: 
        answercount = int(text[1])
        date = str(text[2])
        question = str(text[4])
        view_weight = (int(text[5]) // 50) + 1 # weight to improve topic mining
        answer = str(text[6])
        datenorm = datetime.datetime.strptime(date, '%Y/%m/%d')
        datenum = int(datenorm.strftime('%Y%m%d'))
        # change datenum limitation to control weeks
        if datenum >= 20190321:
            alltextlist.append(question) # use append or just use '+' to aggregate string
            if answercount > 0 : 
                for i in range(view_weight): # use view_weight to add weight
                    alltextlist.append(answer)
            # print(date, question, view_weight, answer)
    # print(alltextlist)
    return alltextlist

def text_clean_set():
    stop = stopwords.words('english')
    stop.extend(['movies', 'movie' 
        'shows', 'show',
        'films', 'film',
        'tv', 'television'])
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()
    return stop, exclude, lemma


def text_clean(text):
    stop, exclude, lemma= text_clean_set()
    num_free = re.sub(r'\d+', '', text)
    punc_free = re.sub("—", "", num_free)
    punc_free0 = re.sub("\'", "", punc_free)
    punc_free1 = "".join(ch for ch in punc_free0 if ch not in exclude)
    stop_free1 = " ".join([i for i in punc_free1.lower().split() if i not in stop])
    punc_free2 = "".join(ch for ch in stop_free1 if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free2.split())
    return normalized


def text_clean_run():
    text_cleaned0 = [] # text_cleaned0 has only one list
    alltextlist = classify_doc()
    text_cleaned2 = [text_clean(text).split() for text in alltextlist] 
    fw = open('./textfiles/Mar4, 2019.txt', 'w')
    for list1 in text_cleaned2:
        for list2 in list1:
            text_cleaned0.append(list2)
            if list2 == "": continue
            else:
                list2 = list2 + "\t"
                fw.write(list2)

    # fr = open('./textfiles/Mar4, 2019.txt', 'r')
    # print(fr.read())
    # print(text_cleaned0) # text_cleaned2 has many lists in list
    return text_cleaned2, text_cleaned0


def btm_model():
    texts = open('./textfiles/Mar4, 2019.txt').read().splitlines()

    # vectorize texts
    vec = CountVectorizer(stop_words='english')
    X = vec.fit_transform(texts).toarray()

    # get vocabulary
    vocab = np.array(vec.get_feature_names())

    # get biterms
    biterms = vec_to_biterms(X)

    # create btm
    btm = oBTM(num_topics=20, V=vocab)

    print("\n\n Train Online BTM ..")
    for i in range(0, len(biterms), 100): # prozess chunk of 200 texts
        biterms_chunk = biterms[i:i + 100]
        btm.fit(biterms_chunk, iterations=50)
    topics = btm.transform(biterms)



def lda_model():
    text_cleaned2, text_cleaned0 = text_clean_run()
    dictionary = corpora.Dictionary(text_cleaned2)
    # dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_cleaned2]
    # using Bag of Words
    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=50)
    print(ldamodel.print_topics(num_topics=5, num_words=8))
    # Compute Perplexity
    print('\nPerplexity: ', ldamodel.log_perplexity(doc_term_matrix))  # a measure of how good the model is. lower the better.
    # Compute Coherence Score
    coherence_model_lda = CoherenceModel(model=ldamodel, texts=text_cleaned2, dictionary=dictionary, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()
    print('\nCoherence Score: ', coherence_lda)


def tfidf_model():
    text_cleaned2, text_cleaned0  = text_clean_run()
    dictionary = corpora.Dictionary(text_cleaned2)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_cleaned2]
    # using TF-IDF
    Lda = gensim.models.ldamodel.LdaModel
    tfidf = models.TfidfModel(doc_term_matrix)
    corpus_tfidf = tfidf[doc_term_matrix]
    ldamodel_tfidf = Lda(corpus_tfidf, num_topics=10, id2word = dictionary, passes=50)
    print(ldamodel_tfidf.print_topics(num_topics=10, num_words=5))

    # Compute Perplexity
    print('\nPerplexity: ', ldamodel_tfidf.log_perplexity(doc_term_matrix))  # a measure of how good the model is. lower the better.
    # Compute Coherence Score
    coherence_model_lda = CoherenceModel(model=ldamodel_tfidf, texts=text_cleaned2, dictionary=dictionary, coherence='c_v')
    coherence_tfidf = coherence_model_lda.get_coherence()
    print('\nCoherence Score: ', coherence_tfidf)


def kmeans_model():
    num_clusters = 5
    km = KMeans(n_clusters = num_clusters)
    text_cleaned2, text_cleaned0 = text_clean_run()
    dictionary = corpora.Dictionary(text_cleaned2)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_cleaned2]
    # using TF-IDF and Clusterclear
    tfidf = models.TfidfModel(doc_term_matrix)
    corpus_tfidf = tfidf[doc_term_matrix]
    km.fit(text_cleaned0)
    clusters = km.labels_.tolist()
    print(clusters)


def get_wordfrequency():
    text_cleaned2, text_cleaned0  = text_clean_run()
    print(collections.Counter(text_cleaned0))


if __name__ == "__main__":
    # lda_model()
    # tfidf_model()
    # kmeans_model()
    get_wordfrequency()


    # 写出lda的循环调参并绘图