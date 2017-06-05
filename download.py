def download(query):
    from cs50 import SQL
    import json
    import requests
    from urllib import parse
    from time import sleep
    import nltk
    
    
    # configure CS50 Library to use SQLite database
    db = SQL("sqlite:///nytimes.db")
    
    
    #api = 50563e044c4e4592acf20db225d80ddf
    #http://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial
    
    urlroot='https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=50563e044c4e4592acf20db225d80ddf&fq=headline:' + str(query) + '&page='
    
    #json_articles = requests.get(urlroot).json() https://www.youtube.com/watch?v=19-LOqdI61k
    
    #nmbrrslts=json_articles['response']['meta']['hits']
    
    
    for j in range(0, 19): #change number of pages to be downloaded
    
        url = str(urlroot + str(j))
        print(j) #test and onscreen counter
        sleep(1.1)
        json_articles = requests.get(url).json()
        
        for i in range(0, 10): #each page has 10 json articles
            
           
            
            #create title
            title=json_articles["response"]["docs"][i]["headline"]["main"] #test
            #print(title) #test
            
            
            #create year
            year=int(json_articles['response']['docs'][i]['pub_date'][:4])
            #print(year) #test
            
            #create abstract aka snippet
            abstract=json_articles['response']['docs'][i]['snippet']
            #print(abstract) #test
            
            #section 
            section=json_articles['response']['docs'][i]['section_name']
            #print(section) #test
            
            db.execute("INSERT INTO articles (title, year, abstract, section) VALUES(:title, :year, :abstract, :section)", title=title, year=year, abstract=abstract, section=section)
    
