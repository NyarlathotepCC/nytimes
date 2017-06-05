import download as first
import analyze as then
import output as and_finally
import string
from cs50 import SQL
import csv

#get inputs
query=input("Please enter your NY Times search term: ")

if len(query.split()) > 1:
    raise Exception("Only single word searches at this stage")

invalidChars = set(string.punctuation.replace("_", ""))
if any(char in invalidChars for char in query):
    raise Exception("No special characters allowed at this stage")
    
# configure CS50 Library to use SQLite database
db = SQL("sqlite:///nytimes.db")

#reset database 
db.execute("DELETE FROM articles")




first.download(query) 
then.analyze()
and_finally.output(query)



