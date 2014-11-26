import re
import porter
from numpy import zeros,dot
from numpy.linalg import norm

__all__=['compare']

# import real stop words
#stop_words = [ 'i', 'in', 'a', 'to', 'the', 'it', 'have', 'was', 'but', 'is', 'be', 'from' ]
stop_words = [w.strip() for w in open('stopword','r').readlines()]
#print stop_words

splitter=re.compile( "[a-z\-']+", re.I )
stemmer=porter.PorterStemmer()

#create the dictionary, return all the different words and their counts
def add_word(word,d):
    w=word.lower()
    if w not in stop_words:
        ws=stemmer.stem(w,0,len(w)-1)
        d.setdefault(ws,0)
        d[ws] += 1

#calculate a doc's vector space model
def doc_vec(doc,key_idx):
    v=zeros(len(key_idx))
    for word in splitter.findall(doc):
        keydata=key_idx.get(stemmer.stem(word,0,len(word)-1).lower(), None)
	#print keydata
        if( keydata and v[keydata[0]]): v[keydata[0]] += 1
	elif( keydata ): v[keydata[0]] = 1
    return v

#return the cosine value of two documents
def compare(doc1,doc2):

    # strip all punctuation but - and '
    # convert to lower case
    # store word/occurance in dict
    all_words=dict()

    for dat in [doc1,doc2]:
        [add_word(w,all_words) for w in splitter.findall(dat)]
 
    # build an index of keys so that we know the word positions for the vector
    key_idx=dict() # key-> ( position, count )
    keys=all_words.keys()
    keys.sort()
    #print keys
    #print  all_words
    for i in range(len(keys)):
        key_idx[keys[i]] = (i,all_words[keys[i]])
    #del keys
    #del all_words
    #print  key_idx
    v1=doc_vec(doc1,key_idx)
    v2=doc_vec(doc2,key_idx)
    print v1
    #print "\n"
    print v2
    return float(dot(v1,v2) / (norm(v1) * norm(v2)))
 
 
if __name__ == '__main__':
    print "Running Test..."
    doc = dict()
    i = 0 
    for line in  open("original_result"):
	doc[i] = line
        i += 1

    for i in range(0, len(doc)):
	print i 
	print doc[i]
    print "Similarity %s" % compare(doc[5],doc[1])
