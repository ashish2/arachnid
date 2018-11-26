from threading import Thread
from arachqueue import ArachQueue

class BaseCrawler(object):
    """BaseCrawler to be extended by SiteCrawler"""

    def __init__(self, urls):
        """
        Initiation params for the crawler
        """
        #self.id = id
        # Assign urls
        self.urls = urls
        #self.urls = ["x", "y", "z"]
        # Initiate Queue
        self.q = ArachQueue()
        # All threads
        self.all_threads = []
        # Threads
        self.config = {
                    "threads": {
                            "number": 2
                        }
                }
        #self.initiate_queue()
        #self.initiate_threads()


    def initiate_queue(self):
        for i in self.urls:
            self.q.enq(i)
        return True

    def initiate_threads(self):
        for i in range(self.config.get("threads").get("number") ):
            worker = Thread(target=self.crawl, args=[i])
            worker.setName("Thread-"+str(i))
            worker.start()
            self.all_threads.append(worker)
        return True

    #def finish_threads(self):
    #    for t in self.all_threads:
    #        print("thread ", t)
    #        t.join()

    def post(self, url):
        pass




