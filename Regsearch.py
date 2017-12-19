import metapy
import sys
import PyPDF2
import os
import errno
import shutil
from config_operationrequirement import create_config_operationreq
from createcorpusconfig import createcorpusinfo
from labeloutput import trainingalgo
from labeloutput_new import training_algo
from distutils.dir_util import copy_tree
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def reg_search(path):
    os.chdir(path)
    make_sure_path_exists('.\\Requirements')
    make_sure_path_exists('.\\crf')
    make_sure_path_exists('.\\parser')
    make_sure_path_exists('.\\perceptron-tagger')
    shutil.copy2('.\\OperationalRequirement.txt', '.\\Requirements\\Requirements.dat')
    #shutil.copy2('C:\\Users\\Pradeep\\Anaconda3_1\\Lib\\site-packages\\metapy\\lemur-stopwords.txt', 'C:\\Users\\Pradeep\\Anaconda3_1\\Lib\\site-packages\\metapy\\regulations\\lemur-stopwords.txt')
    shutil.copy2('..\\lemur-stopwords.txt','.\\lemur-stopwords.txt')
    create_config_operationreq(path)
    shutil.copy2('.\\line.toml','.\\Requirements\\line.toml')
    #copy_tree(fromDirectory, toDirectory)
    copy_tree("..\\parser", ".\\parser")
    copy_tree("..\\crf",".\\crf")
    copy_tree('..\\perceptron-tagger',".\\perceptron-tagger")
    os.chdir(path)
    search_inv_idx = metapy.index.make_inverted_index('Requirements-config.toml')
    search_fwd_idx = metapy.index.make_forward_index('Requirements-config.toml')
    #search_dset = metapy.classify.MulticlassDataset(search_inv_idx)
    ranker = metapy.index.OkapiBM25()
    query = metapy.index.Document()
    Usersearchquery = input("Enter search query:")
    query.content(str(Usersearchquery))
    top_docs = ranker.score(search_inv_idx,query,num_results = 5)
    for num, (d_id, _) in enumerate(top_docs):
        content = search_inv_idx.metadata(d_id).get('content')
        print("{}. {}...\n".format(num + 1, content[0:250]))

if __name__ == '__main__':
    folderpath = input("Enter Folder path for Search: ")
    reg_search(folderpath)
