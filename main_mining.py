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
import matplotlib.pyplot as plt
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
    fw = open('./textfiles/Ori-Mar4, 2019.txt', 'w')
    for text in alltextlist:
        text = text + "\n"
        fw.write(text)
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
    # free numbers
    num_free = re.sub(r'\d+', '', text)
    # free English abbreviation
    abr_free0 = re.sub("’s", "", num_free)
    abr_free1 = re.sub("’re", "", abr_free0)
    abr_free2 = re.sub("’ve", "", abr_free1)
    abr_free3 = re.sub("’m", "", abr_free2)
    abr_free4 = re.sub("n’t", "", abr_free3)
    # free Chinese puncuation
    punc_free0 = re.sub("–", "", abr_free4)
    punc_free1 = re.sub("—", "", punc_free0)
    punc_free2 = re.sub("\…", "", punc_free1)
    punc_free3 = re.sub("\‘", "", punc_free2)
    punc_free4 = re.sub("\’", "", punc_free3)
    punc_free5 = re.sub("\“", "", punc_free4)
    punc_free6 = re.sub("\”", "", punc_free5)
    # English free
    stop_free = " ".join([i for i in punc_free6.lower().split() if i not in stop])
    punc_free = "".join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


def text_clean_run():
    temp_text = ""
    text_cleaned0 = [] # text_cleaned0 has only one list
    text_cleaned1 = []
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
        temp_text = " ".join(list1)
        text_cleaned1.append(temp_text)
    # print(text_cleaned1) # text_cleaned1 has many single word in lists
    # fr = open('./textfiles/Mar4, 2019.txt', 'r')
    # print(fr.read())
    # print(text_cleaned0) # text_cleaned2 has many lists in list
    return text_cleaned2, text_cleaned1, text_cleaned0


def get_wordfrequency():
    text_cleaned2, text_cleaned1, text_cleaned0  = text_clean_run()
    print(collections.Counter(text_cleaned0))


def lda_model(num_topics):
    num_topics = num_topics
    text_cleaned2, text_cleaned1, text_cleaned0 = text_clean_run()
    dictionary = corpora.Dictionary(text_cleaned2)
    # dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_cleaned2]
    # using Bag of Words
    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(doc_term_matrix, num_topics=num_topics, id2word = dictionary, iterations=50)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=10))
    # Compute Perplexity
    perplexity_lda = ldamodel.log_perplexity(doc_term_matrix)
    print('\nPerplexity: ', perplexity_lda)  # a measure of how good the model is. lower the better.
    # Compute Coherence Score
    coherence_model_lda = CoherenceModel(model=ldamodel, texts=text_cleaned2, dictionary=dictionary, coherence='c_v') # u_mass
    coherence_lda = coherence_model_lda.get_coherence()
    print('\nCoherence Score: ', coherence_lda)
    return perplexity_lda, coherence_lda


def tfidf_model(num_topics):
    num_topics = num_topics
    text_cleaned2, text_cleaned1, text_cleaned0  = text_clean_run()
    dictionary = corpora.Dictionary(text_cleaned2)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_cleaned2]
    # using TF-IDF
    Lda = gensim.models.ldamodel.LdaModel
    tfidf = models.TfidfModel(doc_term_matrix)
    corpus_tfidf = tfidf[doc_term_matrix]
    ldamodel_tfidf = Lda(corpus_tfidf, num_topics=num_topics, id2word = dictionary, iterations=50)
    print(ldamodel_tfidf.print_topics(num_topics=num_topics, num_words=10))

    # Compute Perplexity
    perplexity_tfidf = ldamodel_tfidf.log_perplexity(doc_term_matrix)
    print('\nPerplexity: ', perplexity_tfidf)  # a measure of how good the model is. lower the better.
    # Compute Coherence Score
    coherence_model_tfidf = CoherenceModel(model=ldamodel_tfidf, texts=text_cleaned2, dictionary=dictionary, coherence='c_v')
    coherence_tfidf = coherence_model_tfidf.get_coherence()
    print('\nCoherence Score: ', coherence_tfidf)
    return perplexity_tfidf, coherence_tfidf


def btm_model(num_topics):
    num_topics = num_topics
    # texts = open('./textfiles/Ori-Mar4, 2019.txt').read().splitlines()
    text_cleaned2, texts, text_cleaned0 = text_clean_run()
    # vectorize texts
    vec = CountVectorizer(stop_words='english')
    X = vec.fit_transform(texts).toarray()
    print(X[1:])
    # get vocabulary
    vocab = np.array(vec.get_feature_names())
    # get biterms
    biterms = vec_to_biterms(X)
    # create btm
    btm = oBTM(num_topics = num_topics, V = vocab)
    print("\n\n Train Online BTM ..")
    for i in range(0, 1): # prozess chunk of 200 texts
        biterms_chunk = biterms[i:i + 100]
        btm.fit(biterms_chunk, iterations=10)
    
    print("\n\n Topic coherence ..")
    topic_summuary(btm.phi_wz.T, X, vocab, 15)

    # topics = btm.transform(biterms)
    # print("\n\n Visualize Topics ..")
    # vis = pyLDAvis.prepare(btm.phi_wz.T, topics, np.count_nonzero(X, axis=1), vocab, np.sum(X, axis=0))
    # pyLDAvis.save_html(vis, './textfiles/online_btm.html')

    # print("\n\n Texts & Topics ..")
    # for i in range(len(texts)):
        # print(topics[i].argmax())
        # print("{} (topic: {})".format(texts[i], topics[i].argmax()))


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


def lda_plot():
    epoch_time = 10
    perplexity_ldas = []
    coherence_ldas = []
    for num_topics in range(1, epoch_time + 1):
        perplexity_lda, coherence_lda = lda_model(num_topics)
        perplexity_ldas.append(perplexity_lda)
        coherence_ldas.append(coherence_lda)

    plt.subplot(211)
    X = range(1, epoch_time + 1)
    plt.plot(X, coherence_ldas, label = "lda-coherence")
    plt.xlabel("epoch time")
    plt.ylabel("coherence")
    plt.title("LDA-coherence-graph")
    plt.legend()
    plt.tight_layout()

    plt.subplot(212)
    X = range(1, epoch_time + 1)
    plt.plot(X, perplexity_ldas, label = "lda-perplexity")
    plt.xlabel("epoch time")
    plt.ylabel("perplexity")
    plt.title("LDA-perplexity-graph")
    plt.legend()
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    num_topics = 6
    # lda_model(num_topics)
    # tfidf_model(num_topics)
    btm_model(num_topics)

    # kmeans_model()
    # get_wordfrequency()
    
    # lda_plot()

