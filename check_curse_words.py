import urllib
import os
def read_text():
    path = os.getcwd()
    path = path+os.path.sep+"check.txt"
    quotes = open(path) 
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)    
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    #print(output)
    
    connection.close()
    if "true" in output:
        print ("Profanity Alert - found cousre words")
    elif "false" in output:
        print "This Document has no curse words"
    else:
        print "could'nt scan document properly"
    
read_text()

