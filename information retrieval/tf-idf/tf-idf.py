import nltk
import numpy as np
from numpy import array
from nltk.corpus import stopwords
import sys


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
query = 'president obama'
docN = 60
stop = set(stopwords.words('english'))
stop2 = set([',', '.', '``', '\'\'', '--'])
directory = 'C:/Users/junkyoung/OneDrive/바탕 화면/과제_01/data/'


def cosine_similarity(x, y):
    normalizing_factor_x = np.sqrt(np.sum(np.square(x)))
    normalizing_factor_y = np.sqrt(np.sum(np.square(y)))
    s = 0
    for i in range(len(x)):
        s = s + x[i]*y[i]
    return s/(normalizing_factor_x * normalizing_factor_y)

        
def makeInvertedIndex(index):
    invertedIndex = {}

    for i in range(docN):
        for key in index['doc' + str(i)].keys():
            if invertedIndex.get(key) == None:
                invertedIndex[key] = ['doc'+str(i)]
            else:
                invertedIndex[key].append('doc'+str(i))
    for key in index['query'].keys():
        if invertedIndex.get(key) == None:
            invertedIndex[key] = ['query']
        else:
            invertedIndex[key].append('query')
    
    return invertedIndex


def makeIndexOfQuery():
    tokens = nltk.word_tokenize(query)
    tokens = [j for j in tokens if j not in stop and j not in stop2]
    text = nltk.Text(tokens)
    index = text.vocab()
    return dict(index)


def makeIndex(i):
    f = open(directory + str(i) +'.txt', 'r', encoding='UTF8')
    data = f.read()
    data = data.translate(non_bmp_map)
    data = data.lower()
    tokens = nltk.word_tokenize(data)
    tokens = [j for j in tokens if j not in stop and j not in stop2]
    text = nltk.Text(tokens)
    index = text.vocab()
    f.close
    return dict(index)


class Search:
    def __init__(self):
        index = {}
        for i in range(docN):
            index['doc' + str(i)] = makeIndex(i)
        index['query'] = makeIndexOfQuery()

        invertedIndex = makeInvertedIndex(index)
        tf_idf = [[0]*len(invertedIndex) for i in range(docN+1)]
        for word in invertedIndex.keys():
            for doc in invertedIndex[word]:
                tf = index[doc][word]
                idf = docN+1 / len(invertedIndex[word])
                tf_idf[list(index.keys()).index(doc)][list(invertedIndex.keys()).index(word)] = np.log(1 + tf) * np.log(idf)
                
        print('========== Inverted Index ==========')
        print('president: ')
        print(invertedIndex['president'])
        print('\nobama: ')
        print(invertedIndex['obama'])
        print('\n')

        print('========== Term-Document Incidence Matrix ==========')
        print('president: ')
        for i in range(docN):
            print(tf_idf[i][list(invertedIndex.keys()).index('president')], end=' ')
        print('\n\nobama: ')
        for i in range(docN):
            print(tf_idf[i][list(invertedIndex.keys()).index('obama')], end=' ')
        print('\n')

        rank = {}
        score = [0 for i in range(docN+1)]
     
        for i in range(docN):
            if 'doc'+str(i) in invertedIndex['president'] or 'doc'+str(i) in invertedIndex['obama']:
                score[i] = cosine_similarity(tf_idf[docN], tf_idf[i])
                rank[score[i]] = str(i) + '.txt'
        score.sort(reverse = True)
        print('\n========== Top5 Documents ==========')
        for i in range(5):
            print(str('rank'+str(i+1)+': ' + rank[score[i]]) + ' score: ' + str(score[i]))
        print('\n')
                        
if __name__ == '__main__':
    search = Search()
