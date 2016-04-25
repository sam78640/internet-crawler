import urllib
from urllib import request
import re

# Site crawler class
class Crawler:
    def __init__(self,url):
        self.url_startpoint = url

    def crawl(self):
        print ("Loading...")
        request = urllib.request.Request(self.url_startpoint)
        resp = urllib.request.urlopen(request)
        read = str(resp.read())
        filtered = re.findall(r'<a href="(.*?)"',read)
        return filtered
    
    def store_500(self,url):
        file = open("List-of-all-sites.txt","at")
        write = False
        for urls in url:
            write = False
            include = re.search(r'http://(.*?)',urls)
            try:
                to_include = include.group(0)
                write = True
            except:
                write = False
            if write:
                file.write(urls+"\n")
        file.close()
        
    def run(self):
        urls = self.crawl()
        self.store_500(urls)
for i in range (0,199):
    print (i)
    crawler = Crawler("http://list-of-domains.org/alexa/Alexa_"+str(i)+".html")
    crawler.run()

        
