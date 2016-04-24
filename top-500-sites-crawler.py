import urllib
from urllib import request
import re

# Top 500 Sites on internet
class Crawler:

    def __init__(self):
        self.url_startpoint = "https://moz.com/top500"

    def crawl(self):
        request = urllib.request.Request(self.url_startpoint)
        resp = urllib.request.urlopen(request)
        read = str(resp.read())
        filtered = re.findall(r'<a href="(.*?)"',read)
        self.moz = re.findall(r'<a href="https://moz.com(.*?)"',read)
        return filtered
    def store_500(self,url):
        file = open("Top-500.txt","at")
        for urls in url:
            write = True
            for i in self.moz:
                if urls == "https://moz.com"+str(i):
                    write = False
            if write:
                file.write(urls+"\n")
        file.close()
        
    def run(self):
        urls = self.crawl()
        self.store_500(urls)

crawler = Crawler()
crawler.run()

        
