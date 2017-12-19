import os
from contextlib import contextmanager
#from grizzled.os import working_directory

def createcorpusinfo(path):
    currentpath = os.getcwd()
    os.chdir(path)
    currentpath = os.getcwd()
    #print (currentpath)
    config = """type = "line-corpus"
store-full-text = true
encoding = "utf-8"
        """
    with open('line.toml', 'w') as f:
        f.write(config)
        f.close()

    #os.chdir('C:\\Users\\Pradeep\\Anaconda3_1\\Lib\\site-packages\\metapy')
   # currentpath = os.getcwd()
    #print (currentpath)