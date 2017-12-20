# Automatic Extraction of Regulatory Obligations

Simple library and command line utility to extract regulatory obligations from regulatory pdf documents.

The package utilizes PyPDF2 to extract text from pdf document. The package applies Support vector machine algorithm implementation of Metapy Tool Kit to label and extract label regulatory obligations.
The Package also utilizes SUMY implementation of LSA Text summarization algorithm to summarize regulatory obligations.



# Installation


We'll use [metapy](https://github.com/meta-toolkit/metapy)---Python bindings for MeTA. 


We'll use [SUMY](https://github.com/miso-belica/sumy) for text summarization

We'll use [PyPDF2](https://github.com/mstamy2/PyPDF2) for text extraction from pdf document

# Install Metapy

pip install metapy pytoml

# Install PyPDF2

pip install PyPDF2

# Install SUMY Text summarizer

pip install sumy

## Setup
Download/Clone the repository to your local folder
If you have downloaded the repository correctly you would see the following folders/files in your local

- Regulatory_obligation_extraction : Main folder

- Regulatory_obligation_extraction/crf

- Regulatory_obligation_extractionparser

- Regulatory_obligation_extraction/perceptron-tagger

- Regulatory_obligation_extraction/training

- createconfig.py

- createcorpusconfig.py

- labeloutput.py

- labeloutput_new.py

- lemur-stopwords.txt

- processpdf.py

- Regsearch.py

- Summarizer.py

- training-config.toml

## Regulatory document
Place any regulatory document in pdf format downloaded from regulator's website with in the main folder and the run the processpdf.py file through command prompt

#processpdf.py

Provide the folder path where the regulatory document is placed

Provide the full name of the regularoty document

Process would create an output called summary.txt which would contain all the key rules mentioned in the regulatory document.


