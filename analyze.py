def analyze():
    from cs50 import SQL
    import json
    import requests
    from urllib import parse
    from time import sleep
    import nltk
    import os
    import sys
    from analyzer import Analyzer     #credits to doug and doug alone for the orig version of analyzer
    from nltk.tokenize import TweetTokenizer
    
    # configure CS50 Library to use SQLite database
    db = SQL("sqlite:///nytimes.db")
    
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    
    #source for txt: Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, Washington, USA, 
    
    #instantiate it
    tknzr = TweetTokenizer()
    analyzer = Analyzer(positives, negatives)
    
    counter = db.execute("SELECT COUNT (id) FROM articles")[0]['COUNT (id)']
    #print(counter)
    
    #iterate over articles from 0 to number of articles
    
    
    for a in range(1, counter+1):
        positive_words=0
        negative_words=0
        
        #load title of article
        titlestring=db.execute("SELECT title FROM articles")[a-1]['title'] #replace number with loop counter
       
        tempwords=tknzr.tokenize(titlestring) #tokenize title into array
        
        while "’" in tempwords:            #clean title
           tempwords.remove("’")
        while "," in tempwords:            #clean title
            tempwords.remove(",")
        while "." in tempwords:            #clean title
           tempwords.remove(".")
        while "‘" in tempwords:            #clean title
           tempwords.remove("‘")
        while "'" in tempwords:            #clean title
           tempwords.remove("'")
        while ":" in tempwords:            #clean title
           tempwords.remove(":")
        
        #print(tempwords)
        
        for o in range(len(tempwords)):
           
            temp=analyzer.analyze(tempwords[o])
            if temp == 1:
                positive_words=positive_words+1
                #print(tempwords[o])
            if temp == -1:
                negative_words=negative_words+1
                #print(tempwords[o])
        
        
        
        #same analysis for abstract of news article
        
        abstractstring=db.execute("SELECT abstract FROM articles")[a-1]['abstract'][:-4] #last four chars get omitted because it is always "...."
        #print(abstractstring)
        
        #tokenize title into array
        tempabstractwords=tknzr.tokenize(abstractstring)
        
        while "’" in tempabstractwords:            #clean abstract
           tempabstractwords.remove("’")
        while "," in tempabstractwords:            #clean abstract
            tempabstractwords.remove(",")
        while "." in tempabstractwords:            #clean abstract
           tempabstractwords.remove(".")
        while "‘" in tempabstractwords:            #clean abstract
           tempabstractwords.remove("‘")
        while "'" in tempabstractwords:            #clean abstract
           tempabstractwords.remove("'")
        while ":" in tempabstractwords:            #clean abstract
           tempabstractwords.remove(":")
        
        
        for e in range(len(tempabstractwords)):
           
            temp=analyzer.analyze(tempabstractwords[e])
            if temp == 1:
                positive_words=positive_words+1
                #print(tempabstractwords[e])
            if temp == -1:
                negative_words=negative_words+1
                #print(tempabstractwords[e])
        
        
        
        #print(positive_words) 
        #print(negative_words)
        
        db.execute("UPDATE articles SET pos_words = :pos_words WHERE id=:idd", pos_words=positive_words, idd=a) #put at end
        db.execute("UPDATE articles SET neg_words = :neg_words WHERE id=:idd", neg_words=negative_words, idd=a) #put at end
        
