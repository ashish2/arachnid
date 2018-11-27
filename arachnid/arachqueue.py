import multiprocessing
from multiprocessing.queues import Queue


class ArachQueue(Queue):
    """
    Class to store all urls to be crawled
    """

    def __init__(self):
        """Constructor to create a Queue implementation with help of a List()"""
        maxsize = 10
        super().__init__(maxsize, ctx=multiprocessing.get_context())

    def enq(self, url):
        """Inserts the url at 0 index, in accordance with the FIFO method"""
        print("ENQ: " , url)
        ret = self.put(url)
        return ret

    def deq(self):
        """Returns the url which got inserted earliest, in accordance with the FIFO method"""
        if self.empty():
            #raise Exception
            return None
        ret = self.get()
        return ret


#q = ArachQueue()

