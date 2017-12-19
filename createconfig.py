import metapy
import sys
import os

def create_configfile(path):
    config = """prefix = "."
dataset = "regulations"
corpus = "line.toml"
index = "regulations-idx"
stop-words = "lemur-stopwords.txt"
    
[[analyzers]]
method = "ngram-word"
ngram = 1
filter = "default-unigram-chain"
    
[[analyzers]]
method = "ngram-word"
ngram = 2
filter = "default-unigram-chain"
    
[[analyzers]]
method = "ngram-pos"
ngram = 2
filter = [{type = "icu-tokenizer"}, {type = "ptb-normalizer"}]
crf-prefix = "crf" 
"""
    cwd = os.getcwd()
    if cwd == path:
        os.chdir(path)
        with open('regulations-config.toml', 'w') as f:
            f.write(config)
    else:
        os.chdir(path)
        with open('regulations-config.toml', 'w') as f:
            f.write(config)
    os.chdir(path)

	
if __name__ == '__main__':
    create_configfile()