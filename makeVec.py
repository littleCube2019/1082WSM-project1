from Parser import Parser
import pickle
import math
import util
import nltk


class myVectorSpace:
    
    def __init__(self):
        self.ps = Parser() #parser from demo
        self.Word2Idx = {}  
        self.DocVec = {} # docId : vector
        self.NounAndVerbIdx = []  # for Nouns and Verb version
        self.CleanVocabulary()
        self.MakeDocumentVec()
    def CleanVocabulary(self):
        f=open("./DocumentList","r")
        s = []
    
        while 1:
            ID = f.readline()
            string = f.readline()
            
            if not ID:
                break

            string = self.ps.tokenise(string)
            string = self.ps.removeStopWords(string)
            s+=string
 
        s = util.removeDuplicates(s)
        
        r=nltk.word_tokenize(" ".join(s))
        tags = set(['VB','NN'])
        pos_tags =nltk.pos_tag(r)


        for i,word in enumerate(s):  
            self.Word2Idx[word] = i
            
        for word,pos in pos_tags:
            if word in self.Word2Idx and pos in tags:
                self.NounAndVerbIdx.append(self.Word2Idx[word])
        


        f.close()

    def MakeVec(self,string):
        vec = [0] * len(self.Word2Idx)
        
        string = self.ps.tokenise(string)
        string = self.ps.removeStopWords(string)
        

        for word in string:
            vec[self.Word2Idx[word]] +=1
        return vec

    def MakeDocumentVec(self):
        f = open("./DocumentList","r")
        while 1:
            ID = f.readline()
            content = f.readline()
            
            if not ID:
                break
            
            ID = int(ID)
            #print(ID) test
            self.DocVec[ID] = self.MakeVec(content)
        f.close()        

          


if __name__ == "__main__":
    test =  myVectorSpace()
    f=open("DocVec.pickle","wb")
    f2 = open("Word2Idx.pickle","wb")
    f3 = open('DfVec.pickle','wb')
    f4 = open('NounAndVerbIdx.pickle','wb')

    pickle.dump(test.DocVec,f)
    pickle.dump(test.Word2Idx,f2)
    pickle.dump(test.NounAndVerbIdx,f4)
    Df = [0] * len(test.Word2Idx)
    for vector in test.DocVec.values():
        count = 0
        for i in vector :
            if i !=0:
                Df[count] +=1 
            count+=1

    
    pickle.dump(Df,f3)

    f.close()
    f2.close()
    f3.close()
    f4.close()


