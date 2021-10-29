'''
@author: Sougata Saha
Institute: University at Buffalo
'''

from tqdm import tqdm
from preprocessor import Preprocessor
from indexer import Indexer
from collections import OrderedDict
from linkedlist import LinkedList
import inspect as inspector
import sys
import argparse
import json
import time
import random
import flask
from flask import Flask
from flask import request
import hashlib
import math

app = Flask(__name__)


class ProjectRunner:
    def __init__(self):
        self.preprocessor = Preprocessor()
        self.indexer = Indexer()

    def _merge(self, list1, list2, type):
        """ Implement the merge algorithm to merge 2 postings list at a time.
            Use appropriate parameters & return types.
            While merging 2 postings list, preserve the maximum tf-idf value of a document.
            To be implemented."""
        # test successfully
        Merge_list = LinkedList()
        pos_1 = list1.start_node
        pos_2 = list2.start_node
        num_of_comp = 0

        if type == 0:
            # merge without skip
            while pos_1 is not None and pos_2 is not None:
                if pos_1.value == pos_2.value:
                    if pos_1.tfidf >= pos_2.tfidf:
                        Merge_list.insert_at_end(pos_1.value, pos_1.tfidf)
                    else:
                        Merge_list.insert_at_end(pos_2.value, pos_2.tfidf)

                    pos_1 = pos_1.next
                    pos_2 = pos_2.next

                elif pos_1.value < pos_2.value:
                    pos_1 = pos_1.next

                else:
                    pos_2 = pos_2.next
                num_of_comp += 1

        else:    # merge with skip
            while pos_1 is not None and pos_2 is not None:
                if pos_1.value == pos_2.value:
                    if pos_1.tfidf >= pos_2.tfidf:
                        Merge_list.insert_at_end(pos_1.value, pos_1.tfidf)

                    else:
                        Merge_list.insert_at_end(pos_2.value, pos_2.tfidf)

                    pos_1 = pos_1.next
                    pos_2 = pos_2.next

                elif pos_1.value < pos_2.value:   # list1 need skip cmp+1
                    if pos_1.skip is not None and pos_1.skip.value < pos_2.value:
                        while pos_1.skip is not None and pos_1.skip.value < pos_2.value:
                            pos_1 = pos_1.skip
                            num_of_comp += 1
                    else:
                        pos_1 = pos_1.next

                else:
                    if pos_2.skip is not None and pos_2.skip.value < pos_1.value:
                        while pos_2.skip is not None and pos_2.skip.value < pos_1.value:
                            pos_2 = pos_2.skip
                            num_of_comp += 1
                    else:
                        pos_2 = pos_2.next

                num_of_comp += 1

            Merge_list.add_skip_connections()

        #print("merge times")
        # print("Merge", Merge_list.length,  Merge_list.traverse_list())
        return Merge_list, num_of_comp

    def _daat_and(self, q_terms, skip_type):
        """ Implement the DAAT AND algorithm, which merges the postings list of N query terms.
            Use appropriate parameters & return types.
            To be implemented."""

        merge_list_p = None
        p_total_comparisons = 0
        L = len(q_terms)
        test=[]

        if L == 1:
            merge_list_p, merge_list_skip = self._get_postings(q_terms)
        else:
            for i in range (1, L):
                if merge_list_p:
                    # already have values but continue to merge
                    p_list1_p = merge_list_p
                    p_list2_p, p_list2_skip = self._get_postings(q_terms[i])
                    merge_list_p, p_comparisons = self._merge(p_list1_p, p_list2_p, skip_type)
                    p_total_comparisons += p_comparisons
                    test.append(p_comparisons)
                    # p_total_comparisons += p_comparisons + merge_list_p.length-1

                else:
                    # first time
                    p_list1_p, p_list1_skip = self._get_postings(q_terms[i-1])
                    p_list2_p, p_list2_skip = self._get_postings(q_terms[i])
                    merge_list_p, p_comparisons = self._merge(p_list1_p, p_list2_p, skip_type)
                    p_total_comparisons += p_comparisons
                    test.append(p_comparisons)

        # print("Merge",p_total_comparisons,test, merge_list_p.traverse_list())
        return merge_list_p, p_total_comparisons


    def _sorted_list (self, Merge_list):
        ''' input a list with incresing ID, sorted with tfidf scores '''
        Dict = []
        pos = Merge_list.start_node
        while pos is not None:
            Dict.append([pos.value, pos.tfidf])
            pos = pos.next

        _dict = sorted(Dict, key=(lambda x: x[1]), reverse=True)
        sort_dict = [i[0] for i in _dict]

        return sort_dict


    def _get_postings(self, term):
        """ Function to get the postings list of a term from the index.
            Use appropriate parameters & return types.
            To be implemented."""

        postings = self.indexer.inverted_index[term]
        # skip_postings = self.indexer.inverted_index[term].traverse_skips()
        skip_postings = LinkedList()
        pos = self.indexer.inverted_index[term].start_node

        while pos is not None:
            skip_postings.insert_at_end(pos.value, pos.tfidf)
            pos = pos.skip

        return postings,  skip_postings


    def _output_formatter(self, op):
        """ This formats the result in the required format.
            Do NOT change."""
        if op is None or len(op) == 0:
            return [], 0
        op_no_score = [int(i) for i in op]
        results_cnt = len(op_no_score)
        return op_no_score, results_cnt

    def run_indexer(self, corpus):
        """ This function reads & indexes the corpus. After creating the inverted index,
            it sorts the index by the terms, add skip pointers, and calculates the tf-idf scores.
            Already implemented, but you can modify the orchestration, as you seem fit."""
        # process logic
        prep_corpus = {}
        with open(corpus, 'r') as fp:
            for line in tqdm(fp.readlines()):
                doc_id, document = self.preprocessor.get_doc_id(line)
                # test tfidf
                tokenized_document = self.preprocessor.tokenizer(document)
                #tokenized_document= self.preprocessor.tokenizer(document)
                prep_corpus[doc_id] = tokenized_document
                #update method .update({doc_id: tokenized_document})
                self.indexer.generate_inverted_index(doc_id, tokenized_document)
        # print(prep_corpus[154053])
        self.indexer.sort_terms()
        self.indexer.add_skip_connections()
        self.indexer.calculate_tf_idf(prep_corpus)
        # print( self.indexer.inverted_index)

    def sanity_checker(self, command):
        """ DO NOT MODIFY THIS. THIS IS USED BY THE GRADER. """

        index = self.indexer.get_index()
        kw = random.choice(list(index.keys()))
        return {"index_type": str(type(index)),
                "indexer_type": str(type(self.indexer)),
                "post_mem": str(index[kw]),
                "post_type": str(type(index[kw])),
                "node_mem": str(index[kw].start_node),
                "node_type": str(type(index[kw].start_node)),
                "node_value": str(index[kw].start_node.value),
                "command_result": eval(command) if "." in command else ""}

    def run_queries(self, query_list, random_command):
        """ DO NOT CHANGE THE output_dict definition"""
        output_dict = {'postingsList': {},
                       'postingsListSkip': {},
                       'daatAnd': {},
                       'daatAndSkip': {},
                       'daatAndTfIdf': {},
                       'daatAndSkipTfIdf': {},
                       'sanity': self.sanity_checker(random_command)}

        for query in tqdm(query_list):
            """ Run each query against the index. You should do the following for each query:
                1. Pre-process & tokenize the query.
                2. For each query token, get the postings list & postings list with skip pointers.
                3. Get the DAAT AND query results & number of comparisons with & without skip pointers.
                4. Get the DAAT AND query results & number of comparisons with & without skip pointers, 
                    along with sorting by tf-idf scores."""
            #raise NotImplementedError

            # 1
            input_term_arr = self.preprocessor.tokenizer(query)  # Tokenized query.
            print ("here", input_term_arr, sorted(input_term_arr) )


            # 2
            term_sort=[]
            for term in input_term_arr:
                postings_list, skip_postings_list = self._get_postings(term)

                postings = postings_list.traverse_list()
                skip_postings = skip_postings_list.traverse_list()

                """ Implement logic to populate initialize the above variables.
                    The below code formats your result to the required format.
                    To be implemented."""
                term_sort.append([term, postings_list.length])
                output_dict['postingsList'][term] = postings
                output_dict['postingsListSkip'][term] = skip_postings


            _dict = sorted(term_sort, key=(lambda x: x[1]))
            input_term_arr = [i[0] for i in _dict]  # yes  increasing order for term list


            # 3  #merge_list, total_comparisons = self._daat_and(input_term_arr)
            merge_list_p, p_total_comparisons = self._daat_and(input_term_arr,0)
            merge_list_skip, skip_total_comparisons = self._daat_and( input_term_arr, 1)
            merge_p_sort = self._sorted_list(merge_list_p)
            merge_skip_sort = self._sorted_list(merge_list_skip)


            and_op_no_skip, and_op_skip, and_op_no_skip_sorted, and_op_skip_sorted = merge_list_p.traverse_list(), merge_list_skip.traverse_list(), merge_p_sort, merge_skip_sort
            and_comparisons_no_skip, and_comparisons_skip, \
                and_comparisons_no_skip_sorted, and_comparisons_skip_sorted = p_total_comparisons, skip_total_comparisons ,p_total_comparisons, skip_total_comparisons

            # Generate right format out_put
            """ Implement logic to populate initialize the above variables.
                The below code formats your result to the required format.
                To be implemented."""
            and_op_no_score_no_skip, and_results_cnt_no_skip = self._output_formatter(and_op_no_skip)
            and_op_no_score_skip, and_results_cnt_skip = self._output_formatter(and_op_skip)
            and_op_no_score_no_skip_sorted, and_results_cnt_no_skip_sorted = self._output_formatter(and_op_no_skip_sorted)
            and_op_no_score_skip_sorted, and_results_cnt_skip_sorted = self._output_formatter(and_op_skip_sorted)

            output_dict['daatAnd'][query.strip()] = {}
            output_dict['daatAnd'][query.strip()]['results'] = and_op_no_score_no_skip
            output_dict['daatAnd'][query.strip()]['num_docs'] = and_results_cnt_no_skip
            output_dict['daatAnd'][query.strip()]['num_comparisons'] = and_comparisons_no_skip

            output_dict['daatAndSkip'][query.strip()] = {}
            output_dict['daatAndSkip'][query.strip()]['results'] = and_op_no_score_skip
            output_dict['daatAndSkip'][query.strip()]['num_docs'] = and_results_cnt_skip
            output_dict['daatAndSkip'][query.strip()]['num_comparisons'] = and_comparisons_skip

            output_dict['daatAndTfIdf'][query.strip()] = {}
            output_dict['daatAndTfIdf'][query.strip()]['results'] = and_op_no_score_no_skip_sorted
            output_dict['daatAndTfIdf'][query.strip()]['num_docs'] = and_results_cnt_no_skip_sorted
            output_dict['daatAndTfIdf'][query.strip()]['num_comparisons'] = and_comparisons_no_skip_sorted

            output_dict['daatAndSkipTfIdf'][query.strip()] = {}
            output_dict['daatAndSkipTfIdf'][query.strip()]['results'] = and_op_no_score_skip_sorted
            output_dict['daatAndSkipTfIdf'][query.strip()]['num_docs'] = and_results_cnt_skip_sorted
            output_dict['daatAndSkipTfIdf'][query.strip()]['num_comparisons'] = and_comparisons_skip_sorted

        return output_dict

# # #
@app.route("/execute_query", methods=['POST'])
def execute_query():
    """ This function handles the POST request to your endpoint.
        Do NOT change it."""
    start_time = time.time()

    queries = request.json["queries"]
    random_command = request.json["random_command"]

    """ Running the queries against the pre-loaded index. """
    output_dict = runner.run_queries(queries, random_command)

    """ Dumping the results to a JSON file. """
    with open(output_location, 'w') as fp:
        json.dump(output_dict, fp)

    response = {
        "Response": output_dict,
        "time_taken": str(time.time() - start_time),
        "username_hash": username_hash
    }
    return flask.jsonify(response)


if __name__ == "__main__":
    """ Driver code for the project, which defines the global variables.
        Do NOT change it."""

    output_location = "project2_output.json"
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--corpus", type=str, help="Corpus File name, with path.")
    parser.add_argument("--output_location", type=str, help="Output file name.", default=output_location)
    parser.add_argument("--username", type=str,
                        help="Your UB username. It's the part of your UB email id before the @buffalo.edu. "
                             "DO NOT pass incorrect value here")

    argv = parser.parse_args()

    corpus = argv.corpus
    output_location = argv.output_location
    username_hash = hashlib.md5(argv.username.encode()).hexdigest()


    print(corpus, username_hash)


    """ Initialize the project runner"""
    runner = ProjectRunner()

    """ Index the documents from beforehand. When the API endpoint is hit, queries are run against
        this pre-loaded in memory index. """
    runner.run_indexer(corpus)

    ## HERE uncomment
    app.run(host="0.0.0.0", port=9999)
    print("test*******")
# ### test code
# #
#     query1 = ["the novel coronavirus"]
# #     query2 = ['from an epidemic to a pandemic']
#     tokenized_document = runner.preprocessor.tokenizer(query1[0])
#     print(tokenized_document)
#     postings1, postings1_skip = runner._get_postings(tokenized_document[0])
#     postings2, postings2_skip = runner._get_postings(tokenized_document[1])
#     merge_list_p, p_total_comparisons = runner._daat_and(tokenized_document, 0)
#
#     def tran_score(posting):
#
#         KK=[]
#         pp = posting.start_node
#         while pp is not None:
#             KK.append(pp.tfidf)
#         #print(KK)
#         return KK
#     print("test1:", tran_score(postings1))
#     print("test2:", tran_score(postings2))
#     print("test2:", tran_score(merge_list_p))
#
#
# #     merge_list_skip, skip_total_comparisons = runner._daat_and_skip(tokenized_document)
# #     D= runner._sorted_list (merge_list_p)
# #     print(D)
#
