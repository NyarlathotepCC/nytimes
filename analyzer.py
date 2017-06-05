import nltk

class Analyzer():
    """Implements sentiment analysis."""
   


    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        self.positives=[]
        self.negatives=[]
        
        # TODO
        pos = open("positive-words.txt", "r")    
        for line in pos:
            if str.startswith(line, ";") or line.strip()=="":
                    next(pos)
            else:
                freshline=line.strip()
                self.positives.append(freshline.split())    #this bish only appends chars yeah
        pos.close()
        x=0                
        neg = open("negative-words.txt", "r")    
        for line in neg:
            
            if str.startswith(line, ";") or line.strip()=="":
                    next(neg)
            else:
                freshline=line.strip()
                self.negatives.append(freshline.split())        #stylezZz yall
                
        neg.close()
        
        self.flattened_positives = [y for x in self.positives for y in x]  #shortcut found at https://coderwall.com/p/rcmaea/flatten-a-list-of-lists-in-one-line-in-python
       
        self.flattened_negatives = [y for x in self.negatives for y in x]





    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        summe=0
        #for i in range(len(text)):
            
        if str.lower(text) in self.flattened_positives: 
            summe=summe+1                                        
        elif str.lower(text) in self.flattened_negatives:
            summe=summe-1
        
        return summe
        
        '''
        textlist=[]
        summe=0
        
        textlist.append(text.split())
        for i in range(len(textlist[0])):
            if textlist[0][i] in self.positives:
                summe=summe+1
            elif textlist[0][i] in self.negatives:
                summe=summe-1
           # print(textlist[0][i])
        return summe
        '''
