from BeautifulSoup import BeautifulSoup
import urllib2
import re

_WIKIPEDIA = 'https://en.wikipedia.org'

def get_wiki_page(link):
    store = []
    html_page = urllib2.urlopen(link)
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        if bool(link.get('title')):
            links = link.get('href')
            if bool(links):
                if bool(re.match('/wiki/',links)):
                    store.append(links)
    return store

def bfs_path(start , end):
    m = [[start]]
    while True:
        i = m.pop()
        print i
        for value in get_wiki_page(i[-1]):
            check_end = _WIKIPEDIA + value
            if check_end not in i:                  #ensure that links do not point backwards
                if check_end == end:
                    return i + [check_end]
                m=([i+[check_end]]) + m
        
        
        
    
#get_wiki_page('https://en.wikipedia.org/wiki/Ernest_Rutherford') 
#print bfs_path('https://en.wikipedia.org/wiki/Ernest_Rutherford', 'https://en.wikipedia.org/wiki/Electrochemistry')
print bfs_path('https://en.wikipedia.org/wiki/Hari_Bahadur_Rai','https://en.wikipedia.org/wiki/Category:Nepalese_feminists')