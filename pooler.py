import random
import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
from filter import filter
import pandas as pd
import queue
 
class pooler():

    def __init__(self) -> None:
        self.no_of_workers = 5
        self.get_df = pd.DataFrame()
        # self.q = queue.Queue()
        
    def pool(self,fn,q:queue.Queue):
        with ThreadPoolExecutor(max_workers=self.no_of_workers,thread_name_prefix="ticket_pooler") as tpool:
            tpool.map(fn,q)
        print("Batch completed")
            # tpool_active_threads = current_thread().__getattribute__()
            # print(tpool_active_threads)
        # tpool.shutdown(wait=True)

    def put_q(self,df:pd.DataFrame,q:list):
        print("Adding to queue:",df[df.columns[0]].count(),"rows")
        for i,j in df.iterrows():
            q.append(j)
            print ("P:", j["number"])
        print("Added to Queue")
        return q

    def get_q(self,q:queue.Queue):
        print("Fetching from queue:")
        loop = 0
        while not q.empty():
            self.get_df = q.get()
            print ("get (loop: {})".format(loop))
            loop += 1
            print("get",self.get_df)

# po1.get_q(q)
# print(df)

