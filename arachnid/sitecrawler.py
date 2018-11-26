import requests
from bs4 import BeautifulSoup
from basecrawler import BaseCrawler
import arachthread 
#import arachqueue 

class SiteCrawler(BaseCrawler):

    def __init__(self, urls):
        self.urls = urls
        super().__init__(urls)
        print("self.q ", self.q)

    def loop(self):
        # Spawn 4 thread here & each thread will take url from queue 
        # and call the self.get method & write into a DB (text file)
        for i in self.urls:
            # Parse with BS4 and if you find another link, add it to queue
            # Spawn threads to take urls from queue and call those urls
            # insert url into Q
            self.aq.enqueue(i)

        #ArachThread().spawn(self.run)
    
    def get(self, url):
        data = requests.get(url)
        return data

    def runNow(self):
        # if not Queue empty
        # get from queue
        # else 
        # terminate self
        # take urls from self.aq
        # call bs4 & insert in aq again
        if len(aq) > 0:
            pass

    def init_all(self):
        """Initiates Queues and Threads"""
        # Initiate & Insert into Q
        self.initiate_queue()
        # Initiate Threads
        self.initiate_threads()
        #self.finish_threads()

    def call(self):
        for i in li:
            self.q.put(i)

    def crawl(self, wId):
        print("wID: ", wId)
        while not self.q.empty():
            url = self.q.deq()
            if url is not None:
                self.http(url, wId)
        return

    def http(self, url, wId):

        print("Inside HTTP: ", " wID: ", wId)
        res = requests.get(url)
        print("res: ", res)
        print("res.text: ", res.text)
        bs = BeautifulSoup(res.text, 'html.parser')
        links = bs.find_all('a', href=True)

        for link in links:
            self.q.enq(link)

        print("HTTP Qqsize: ", self.q.qsize() )
        return


    def crawlNow(self):
        url = self.urls
        try:
            logging.info("GET " + url)
            res = requests.get(url)
            print("RES ", res)
            bs = BeautifulSoup(res.text)
            # Search for other links & insert into Q
            result[index] = data
        except:
            logging.error("Error while fetching url: " + url)
            result[index] = {}

        return True

    def c(self):
        for i in self.urls:
            print("u ", self.q.bues() )
            self.q.put(i)

        print(self)


#url = ["https://www.google.co.in"]
url = ["http://quotes.toscrape.com/"]
#["https://www.google.co.in"]
s = SiteCrawler(url)


#s.crawl()
s.init_all()
#s.q.join_thread()
for i in s.all_threads:
    i.join()
#print( s.config )



























