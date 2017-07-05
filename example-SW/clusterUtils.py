import gensim
import pickle
from sklearn.cluster import KMeans
import numpy as np

"""
Make Clustering Objects
Takes the kmeans object generated by sklearn, the number of clusters, and the
matrix of word vectors
and uses this to generate a list of clusters formated to contain the number
of unique words in the cluster, the total frequency of those words in the
corpus, and a list of all words, with their associate frequencies
"""
def makeClusteringObjects(word2vecModel,kmeans,vocab_list,WordByFeatureMat):
    clusters =[]
    for i in range(len(kmeans.cluster_centers_)):
        clusters.append( {'unique_words':0,'total_freq':0,'word_list':[]})
    
    predictions = kmeans.predict(WordByFeatureMat)
    for i in range(len(vocab_list)):
        cluster   = predictions[i]
        word      = vocab_list[i]
        freq      = word2vecModel.wv.vocab[word].count
        clusters[cluster]['unique_words'] += 1
        clusters[cluster]['total_freq'] += freq
        clusters[cluster]['word_list'].append((word,freq))
    return clusters


  
    