'''
@author: Sougata Saha
Institute: University at Buffalo
'''

import collections
from nltk.stem import PorterStemmer
import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.ps = PorterStemmer()

    def get_doc_id(self, doc):
        """ Splits each line of the document, into doc_id & text.
            Already implemented"""
        arr = doc.split("\t")
        return int(arr[0]), arr[1]

    def tokenizer(self, text):
        """ Implement logic to pre-process & tokenize document text.
            Write the code in such a way that it can be re-used for processing the user's query.
            To be implemented."""
        # for each doc directly call this function
        doc_str = text
        doc_str = doc_str.lower()          # convert doc to lowercase
        doc_str = re.sub(r'[^\sa-zA-Z0-9]', ' ', doc_str)    # Remove special characters

        doc_str = doc_str.lstrip().rstrip()        # Remove excess whitespaces
        doc_str = re.sub(r'\s{2,}', ' ', doc_str)

        doc_str = re.split(' ', doc_str)    # tokenize doc into terms using white space tokenizer

        # remove stop words
        filtered = [w for w in doc_str if w not in stopwords.words('english')]

        # perform Porter's stemming
        tokens = []
        for i in filtered:
            poterStm = PorterStemmer()
            str_clean = poterStm.stem(str(i))
            tokens.append(str_clean)
        return tokens
        #raise NotImplementedError

# test code
# doc ="2598	Pharmaceutical biotechnology"
# preprocessor = Preprocessor()
# doc_id, document = preprocessor.get_doc_id(doc)
#
# print(doc_id, document)
# tokenized_document = preprocessor.tokenizer( document )
# print(tokenized_document)

# Results
# 2598 Pharmaceutical biotechnology
# ['pharmaceut', 'biotechnolog']





