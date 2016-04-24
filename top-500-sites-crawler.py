import urllib
from urllib import request
import re

# Top 500 Sites on internet
class Crawler:
    def __init__(self,url):
        self.url_startpoint = url

    def crawl(self):
        print ("Loading...")
        request = urllib.request.Request(self.url_startpoint)
        resp = urllib.request.urlopen(request)
        read = str(resp.read())
        filtered = re.findall(r'<a href="(.*?)"',read)
        self.moz = re.findall(r'<a href="https://moz.com(.*?)"',read)
        return filtered
    
    def store_500(self,url):
        file = open("List-of-all-sites.txt","at")
        write = True
        for urls in url:
            write = True
            ignore = re.search(r'javascript:(.*?)',urls)
            try:
                to_ignore = ignore.group(0)
                write = False
            except:
                write = True
            if write:
                file.write(urls+"\n")
        file.close()
        
    def run(self):
        urls = self.crawl()
        self.store_500(urls)
for i in range(0,30):
    crawler = Crawler("http://list-of-domains.org/default.aspx")
    crawler.run()

        
