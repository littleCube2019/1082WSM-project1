from Parser import Parser
import pickle
import util
import math
import numpy
import nltk
from argparse import ArgumentParser



def Print(string , top5):
    print(string,end="\n\n")
    print("DocID     Score")
    for i in reversed(range(5)):
        print(top5[i][0],"  ",abs(top5[i][1]))

def Sort(DocVec,queryVec,dis,top5,r= False,NounAndVerbIdx = []):

    if NounAndVerbIdx == []:
        for ID in DocVec:
            d = dis(DocVec[ID],queryVec)
            if len(top5) < 5:
                top5.append((ID,d))
    
            else:
                top5.append((ID,d))
               
                top5.sort(key = lambda x : x[1],reverse = r)    
                top5.pop(0)

    else:
        NewQuery = []
        for i in NounAndVerbIdx:
            NewQuery.append(queryVec[i])

        for ID in DocVec :
            NewVec = []
            for i in NounAndVerbIdx:
                NewVec.append(DocVec[ID][i])

            d = dis(NewVec,NewQuery)
            if len(top5) < 5:
                top5.append((ID,d))
    
            else:
                top5.append((ID,d))
                top5.sort(key = lambda x : x[1],reverse = r)    
                top5.pop(0)
   
    return top5
                    
def EuclideanDis(vec1,vec2):
    return numpy.linalg.norm(numpy.array(vec1)-numpy.array(vec2)) 

def tfidf(DocVec , DfVec):
    res = {}

    for k,vec in DocVec.items():
        temp = []
        for tf,df in zip(vec,DfVec):
            temp.append(tf*math.log(2048/df,10))
        res[k] = temp
    return res
    
def PseudoFeedback(QueryVec , top1):

    return list(map(lambda q,f : q*1+f*0.5 , QueryVec , top1) )



ArgParse = ArgumentParser()
ArgParse.add_argument("--query",nargs="*",dest="opt")

args = ArgParse.parse_args() 
query = ""
for word in args.opt: #query 
    query += word
    query += " "
query = query[:-1]
parser = Parser()
print(query)
# load vector data 
DocVec = None
Word2Idx = None
DfVec = None
NounAndVerbIdx=None
with open('DocVec.pickle',"rb") as f:
    DocVec = pickle.load(f)
with open('Word2Idx.pickle',"rb") as f:
    Word2Idx = pickle.load(f)
with open('DfVec.pickle','rb') as f:
    DfVec = pickle.load(f)
with open('NounAndVerbIdx.pickle','rb') as f:
    NounAndVerbIdx = pickle.load(f)

# query to vector
query = parser.clean(query)
query = parser.tokenise(query)
query = parser.removeStopWords(query)

QueryVec = [0] * len(Word2Idx)
for word in query:
    if word in Word2Idx:
        QueryVec[Word2Idx[word]] += 1

# tf + cos        

top5 = Sort(DocVec,QueryVec,util.cosine,[])
Print("Term Frequency Weighting + Cosine Similarity:", top5)

# tf + euclidean 
top5 = Sort(DocVec,QueryVec,EuclideanDis,[],True)
Print("Term Frequency Weighting + Euclidean Distance:", top5,)


#tfidf +cos
TfidfTop5 = []
TfIdfVec = tfidf(DocVec , DfVec)
TfidfTop5 =Sort(TfIdfVec,QueryVec,util.cosine,[])
Print("TF-IDF Weighting + Cosine Similarity:",TfidfTop5)


#tfidf + Euclidean
top5 =Sort(TfIdfVec,QueryVec,EuclideanDis,[],True)
Print("TF-IDF Weighting + Euclidean Distance:",top5)

#feedback

TfidfTop5 = Sort(DocVec,PseudoFeedback(QueryVec,TfIdfVec[TfidfTop5[4][0]]),util.cosine,[],False,NounAndVerbIdx)
Print("Feedback Queries + TF-IDF Weighting + Cosine Similarity:",TfidfTop5)






