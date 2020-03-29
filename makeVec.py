from Parser import Parser
import pickle
import math


class myVectorSpace:
    
    def __init__(self):
        self.ps = Parser() #parser from demo
        self.Word2Idx = {}  
        self.DocVec = {} # docId : vector
        
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
            
            s += string

        s = list(set(s))

    
        for i,word in enumerate(s):
            #clean word
            if word in self.Word2Idx:
                print(word)
            self.Word2Idx[word] = i
                
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
    pickle.dump(test.DocVec,f)
    pickle.dump(test.Word2Idx,f2)
    
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

