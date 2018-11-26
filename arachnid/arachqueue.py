import multiprocessing
from multiprocessing.queues import Queue


class ArachQueue(Queue):
    """
    Class to store all urls to be crawled
    """

    def __init__(self):
        """Constructor to create a Queue implementation with help of a List()"""
        #self.urls = list()
        #self.q = Queue()
        maxsize = 10
        super().__init__(maxsize, ctx=multiprocessing.get_context())

    def enq(self, url):
        """Inserts the url at 0 index, in accordance with the FIFO method"""
        print("ENQ: ", url)
        return self.put(url)

    def deq(self):
        """Returns the url which got inserted earliest, in accordance with the FIFO method"""
        print("DEQ")
        if self.empty():
            #raise Exception
            return ("Empty Queue!")
        return self.get()


#q = ArachQueue()

