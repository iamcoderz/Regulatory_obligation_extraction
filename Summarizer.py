from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

#from reportlab.lib.pagesizes import letter
#from reportlab.pdfgen import canvas
#from reportlab.lib.utils import ImageReader
#from PIL import Image


import os


LANGUAGE = "english"
SENTENCES_COUNT = 3

def summarizer_file(path):
    os.chdir(path)
    os.chdir(".\\regulations\\DataClumps")
    filelist = os.listdir(".")
    sorted_files = sorted(filelist, key=lambda x: int(x.split('.')[0]))

    #inputfolderpath = input("Please provide the folder path where the Reg document is available : ")
    # url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
    # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    for filename in sorted_files:
        parser = PlaintextParser.from_file(filename, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            #print(sentence)
            with open('Summary.txt', 'a+') as filesummary:
                filesummary.write(str(sentence) + '\n')

    '''ptr = open("Summary.txt", "r")  # text file I need to convert
    lineas = ptr.readlines()
    ptr.close()
    i = 750
    numeroLinea = 0

    while numeroLinea < len(lineas):
        if numeroLinea - len(lineas) < 60:  # I'm gonna write every 60 lines because I need it like that
            i = 750
            for linea in lineas[numeroLinea:numeroLinea + 60]:
                canvas.drawString(15, i, linea.strip())
                numeroLinea += 1
                i -= 12
            canvas.showPage()
        else:
            i = 750
            for linea in lineas[numeroLinea:]:
                canvas.drawString(15, i, linea.strip())
                numeroLinea += 1
                i -= 12
            canvas.showPage()'''
    return 1


if __name__ == "__main__":
    summarizer_file()