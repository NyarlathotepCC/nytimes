def output(query):
    from cs50 import SQL
    import csv
    
    # configure CS50 Library to use SQLite database
    db = SQL("sqlite:///nytimes.db")
    
    #load title of article
    nmbr_pos_artcls = db.execute("SELECT COUNT (id) FROM articles WHERE pos_words > neg_words")[0]['COUNT (id)']
    print("The number of positive articles is: {}".format(nmbr_pos_artcls))
    
    nmbr_neg_artcls = db.execute("SELECT COUNT (id) FROM articles WHERE pos_words < neg_words")[0]['COUNT (id)']
    print("The number of negative articles is: {}".format(nmbr_neg_artcls))
    
    print("RATIO POSITIVE/NEGATIVE ARTICLES: {}".format(nmbr_pos_artcls/nmbr_neg_artcls))
    
    nmbr_neutr_artcls = db.execute("SELECT COUNT (id) FROM articles WHERE pos_words = neg_words")[0]['COUNT (id)']
    print("(neutral articles: {})".format(nmbr_neutr_artcls))
    print()
    
    nmbr_pos_words=db.execute("SELECT SUM (pos_words) FROM articles")[0]['SUM (pos_words)']
    print("The number of positive words is: {}".format(nmbr_pos_words))
    
    nmbr_neg_words=db.execute("SELECT SUM (neg_words) FROM articles")[0]['SUM (neg_words)']
    print("The number of negative words is: {}".format(nmbr_neg_words))
    
    print("RATIO POSITIVE/NEGATIVE WORDS: {}".format(nmbr_pos_words/nmbr_neg_words))
    print()
    response=str(input("Do you want to save the results to results.csv (y/n): "))
    if response.lower() == "y" or "yes":
        file=open("results.csv", "a")
        writer=csv.writer(file)
        writer.writerow((query, nmbr_pos_artcls, nmbr_neg_artcls, nmbr_pos_artcls/nmbr_neg_artcls, nmbr_neutr_artcls, nmbr_pos_words, nmbr_neg_words, nmbr_pos_words/nmbr_neg_words))
        file.close()
        print("nkay")

    else:
        print("nkay")
