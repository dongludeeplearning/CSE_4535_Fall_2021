'''
@author: Sougata Saha
Institute: University at Buffalo
'''

from linkedlist import LinkedList
from collections import OrderedDict
from preprocessor import Preprocessor

class Indexer:
    def __init__(self):
        """ Add more attributes if needed"""
        self.inverted_index = OrderedDict({})

    def get_index(self):
        """ Function to get the index.
            Already implemented."""
        return self.inverted_index

    def generate_inverted_index(self, doc_id, tokenized_document):
        """ This function adds each tokenized document to the index. This in turn uses the function add_to_index
            Already implemented."""
        for t in tokenized_document:
            self.add_to_index(t, doc_id)

    def add_to_index(self, term_, doc_id_):
        """ This function adds each term & document id to the index.
            If a term is not present in the index, then add the term to the index & initialize a new postings list (linked list).
            If a term is present, then add the document to the appropriate position in the posstings list of the term.
            To be implemented."""
        # test successfully
        if term_ not in self.inverted_index.keys():
            linked_list = LinkedList()
            linked_list.insert_at_end(doc_id_, 0)
            self.inverted_index.update({term_: linked_list})
        else:
            linked_list = self.inverted_index[term_]
            linked_list.insert_at_end(doc_id_, 0)
        #raise NotImplementedError

    def sort_terms(self):
        """ Sorting the index by terms.
            Already implemented."""
        sorted_index = OrderedDict({})
        for k in sorted(self.inverted_index.keys()):
            sorted_index[k] = self.inverted_index[k]
        self.inverted_index = sorted_index


    def add_skip_connections(self):
        """ For each postings list in the index, add skip pointers.
            To be implemented."""
        # test successfully
        for lklist in self.inverted_index.values():
            lklist.add_skip_connections()


    def calculate_tf_idf(self, prep_corpus):
        """ Calculate tf-idf score for each document in the postings lists of the index.
            To be implemented."""
        total_num_docs = len(prep_corpus)   # 5000
        Dict_tfidf = {}
        for item in prep_corpus.keys():      # item : docID
            doc = prep_corpus[item]     # get doc tokenized
            tf_idf_dict = {}                # build dict {term, tf}
            total_terms = len(doc)

            for tm in doc:                    #tcompute term frequence in a doc
                if tm in tf_idf_dict.keys():
                    tf_idf_dict[tm] += 1
                else:
                    tf_idf_dict[tm] = 1

            # compute tf/ total_tokens_in_doc  #{docID: {term: tf_score}}
            for tm_ in tf_idf_dict.keys():
                tf_idf_dict[tm_] = tf_idf_dict[tm_] / total_terms
            Dict_tfidf[item] = tf_idf_dict

        # traverse and update  all the inverted list
        for T in self.inverted_index.keys():
            doc_list = self.inverted_index[T].traverse_list()
            for i in doc_list:
                pos = self.inverted_index[T].start_node
                length = self.inverted_index[T].length
                while pos is not None:
                    tf = Dict_tfidf[i][T]
                    idf = total_num_docs / self.inverted_index[T].length
                    pos.tfidf = tf * idf
                    pos = pos.next
        return


#################################################
# test code
# preprocessor = Preprocessor()
# index = Indexer()
#
# doc ="2518	Pharmaceutical biotechnology"
# doc0 = "3568	Seroprevalence of Pathogens in Wild Rats from the Island of St. Kitts, West Indies"
# doc1 = "6757	Rodent Pathogens in Wild Rats from the Island of St. Kitts, West Indies"
# doc2 = "2568	Seroprevalence of Rodent Rats from the Island of St. Kitts, West Indies"
# doc3 = "6257	Seroprevalence of Rodent Pathogens in Wild Rats from the Island of St. Kitts, West Indies"
# doc4 = "3578	Seroprevalence of Rodent Pathogens in Wild Rats"
# doc5 = "5757	Rats from the Island of St. Kitts, West Indies"
# Doc = [doc, doc0, doc1, doc2, doc3, doc4, doc5]
#
# prep_corpus = {}
# for i in Doc:
#     doc_id, document = preprocessor.get_doc_id(i)
#     tokenized_document = preprocessor.tokenizer(document)
#     prep_corpus.update({doc_id: tokenized_document})
#     index.generate_inverted_index(doc_id, tokenized_document)
#
# #print(index.inverted_index['wild'].traverse_list())
# index.add_skip_connections()
# index.sort_terms()
# index.add_skip_connections()
# index.calculate_tf_idf(prep_corpus)
# print(index.inverted_index['wild'].start_node.tfidf)
