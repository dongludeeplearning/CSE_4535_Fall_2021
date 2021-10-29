# import re
# str= "  sars-cov-2 protein structure"
# print(str.split('-'))
#
# str_1= ' '.join(str.split('-')).split()
# print (str_1)
#
# doc_str = re.sub(r'[^\sa-zA-Z0-9]', ' ', str.lower())
# #doc =re.sub(r'[^\sa-zA-Z0-9]，' '，doc_str)
# print(doc_str)
import math
# L= [23,24,25]
# print(sorted(L reverse=True) )
# Dict =[['te',12],['rr',14],['yy',29],['oo',10],['zz',3]]
#
# _dict = sorted(Dict, key=(lambda x: x[1]), reverse=True)
# sort_dict = [i[0] for i in _dict]
# print(sort_dict)
# Dict = []
# N = len(input_term_arr)
# print(N)
# L = math.floor(N / 2)
# for i in range(L):
#     Dict.append(input_term_arr[i])
#     Dict.append(input_term_arr[N - 1 - i])
# #
# if N & 1 == 1:
#     Dict.append(input_term_arr[L-1])
#
# print(Dict)

# def _sorted_list(Merge_list):
#     ''' input a list with incresing ID, sorted with tfidf scores '''
#     Dict = []
#     pos = Merge_list.start_node
#     while pos is not None:
#         Dict.append([pos.value, pos.tfidf])
#         pos = pos.next
#
#     _dict = sorted(Dict, key=(lambda x: x[1]), reverse=True)
#     sort_dict = [i[0] for i in _dict]
#     return sort_dict

# str = "     INTERFERON: FOR THE COLD AND CANCER?"
#
# print(len(str.split()))
doc=['a', 'b', 'dd','a','cc','dd']
tf_idf_dict={}

for tm in doc:  # compute tf for each doc
    if tm in tf_idf_dict.keys():
        tf_idf_dict[tm] += 1
    else:
        tf_idf_dict[tm] = 1
print (tf_idf_dict)