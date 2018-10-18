#!/usr/bin/env python
# coding: utf8
import urllib
from bs4 import *
import time
import codecs   #never got the special german characters to work right.  Tried to use this.

def get_verbs():
    fhand = codecs.open('verbs.txt', mode = 'r', encoding = 'ascii')    #a .txt file containing the verbs to look up.
    verbs = list()
    for line in fhand:
        verbs.append(line.strip())
    fhand.close()
    return verbs

def write_it(present, past, future):
    fhand = open('verb_output.txt', 'a') # writing output to a .txt file
    fhand.write(present)
    fhand.write('\n')
    fhand.write(past)
    fhand.write('\n')
    fhand.write(future)
    fhand.write('\n')
    fhand.write('\n')
    fhand.close()
    
verbs=get_verbs()
for verb in verbs:
    print verb
    #for every verb in the .txt file, go to the URL, appending the verb to the URL.
    try:
        url="http://www.die-konjugation.de/verb/"+str(verb)+".php"
        my_html = urllib.urlopen(url).read()
        soup = BeautifulSoup(my_html, 'html.parser')
    #pull out all the /div sections containing the class "tempscorps"
        find_me=soup.find_all("div", class_="tempscorps")
    #the present tense was in 0, the next section pulls off /b and br/ returns None,
    #so that is why when it sees None it adds ""
        for i in find_me[0]:
            if (i.string is None):
                i.string = ' '
        present = find_me[0].get_text()
    #perfect past is in 2
        for i in find_me[2]:
            if (i.string is None):
                i.string = ' '
        past = find_me[2].get_text()
    #future is in 4
        for i in find_me[4]:
            if (i.string is None):
                i.string = ' '
        future = find_me[4].get_text()
    
    #write it all out to output
        write_it(present, past, future)
    #try to do it quietly.
        time.sleep(5)
    except:
        print "verb didn't exist"
        pass





    


