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

## Functions used in the Package

Processpdf : process pdf function extracts the text content from the pdf document. Also this function deletes any previous run results from the operating folder.

labeloutput_new : training algo - This function uses the training folder to create a trained SVM object that is used to label the text data from regulatory document that needs to be analyzed. This function also has an algorithm to clump data sets together based on document distance.All the data clumps as well as labelled data content are created by this function.

Summarizer : The summarizer function consumes the data clumps created by training algo in a specific order by squencing the dataclumps.
And creates local summaries and writes the summaries to a Summary document.

Createconfig & Create Corpus functions are support functions that are used to create config files for processing.

Implementation details:

- Train a Document Classifier by labelling Phrases from the regulatory text as “Key Rule” or “TOC” or “Operating Requirement” ..etc..
- Extract text content from a regulatory document using PyPDF2 module.
- Use the trained classifier to label phrases from the document to be evaluated.
- Data Clumping : From the labelled output, clump Co- Occurring Key Rules, Operating Requirements & Reporting Requirements. 
Clumping of documents is performed based on document distance or feature distance measure.  In this current implementation a distance of ‘7’ is used to clump rules together.
- Once Rules are clumped together a Summarizer algorithm is applied to summarize each rule. Each summarized rule is written to a document summary.
- The above document summary will contain all the key rules discussed in the regulatory document.

