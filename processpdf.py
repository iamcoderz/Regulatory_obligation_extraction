import metapy
import sys
import PyPDF2
import os
import shutil
from createconfig import create_configfile
from createcorpusconfig import createcorpusinfo
from labeloutput import trainingalgo
from labeloutput_new import training_algo
from Summarizer import summarizer_file

def remove_non_ascii_1(text):

    return ''.join(i for i in text if ord(i)<128)

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
	
def processpdffile():
    #Need to place file in present working directory of python
    inputfolderpath = input("Please provide the folder path where the Reg document is available : ")
    inputfilename = input("Please provide the input pdf filename with extension:")
    #Outputfilename = input("Output file name")
    #filepath = filepath.replace(""\","\\")
    #print (inputfilename)
    cwd = os.getcwd()
    os.chdir(inputfolderpath)
    print("Deleting previous run folders...")
    try:
        shutil.rmtree('.\\regulations')
        shutil.rmtree('.\\regulations-idx')
        shutil.rmtree('.\\training-idx')
        os.remove('.\\regulations-config.toml')
    except:
        pass
    #if cwd == inputfolderpath:
    try:
        pdfFileOb1 = open(str(inputfilename), 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileOb1)
        filepagecount = pdfReader.numPages
    except:
        print ("File doesnot exist in the folder")
        exit()

    make_sure_path_exists(inputfolderpath + "\\regulations")

    os.chdir(".\\regulations")

    with open('regulations.dat','w') as file1:
    #print("a",file = file1)
        for icount in range(0,pdfReader.numPages):
            pageObj = pdfReader.getPage(icount)
        #templist = pageObj.extractText()
            templist = remove_non_ascii_1(pageObj.extractText())
            for item in templist.split('.\n'):
                if len(item.split()) > 5:
                    print(item.replace('\n', ''), file=file1)
                else:
                    pass

    os.chdir(inputfolderpath)
	
    create_configfile(inputfolderpath)

    corpusfolder = inputfolderpath + "\\regulations"

    createcorpusinfo(corpusfolder)

    os.chdir(inputfolderpath)

    training_algo(inputfolderpath)

    Success = summarizer_file(inputfolderpath)

    if Success == 1:
        print("Regulation Summary Created")

	
if __name__ == '__main__':
    processpdffile()
