'''
@author: Sougata Saha
Institute: University at Buffalo
'''

import math


class Node:

    def __init__(self, value=None, next=None,  skip=None, tfidf=0):
        """ Class to define the structure of each node in a linked list (postings list).
            Value: document id, Next: Pointer to the next node
            Add more parameters if needed.
            Hint: You may want to define skip pointers & appropriate score calculation here"""
        self.value = value
        self.next = next
        self.skip = skip
        self.tfidf = tfidf


class LinkedList:
    """ Class to define a linked list (postings list). Each element in the linked list is of the type 'Node'
        Each term in the inverted index has an associated linked list object.
        Feel free to add additional functions to this class."""
    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.length, self.n_skips, self.idf = 0, 0, 0.0
        self.skip_length = None

    def traverse_list(self):
        traversal = []
        if self.start_node is None:
            print("list has no element!")
            return
        else:
            """ Write logic to traverse the linked list.
                To be implemented."""    ##  add logic here
            pos = self.start_node
            while pos is not None:
                #if pos.value not in traversal:
                traversal.append(pos.value)
                pos = pos.next

            #raise NotImplementedError
            return traversal

    def traverse_skips(self):
        traversal = []
        if self.start_node is None:
            return
        else:
            """ Write logic to traverse the linked list using skip pointers.
                To be implemented."""
            # test successfully
            pos = self.start_node
            while pos is not None:
                if pos.value not in traversal:
                    traversal.append(pos.value)
                pos = pos.skip
            return traversal
            #raise NotImplementedError

    def add_skip_connections(self):
        n_skips = math.floor(math.sqrt(self.length))
        if n_skips * n_skips == self.length:
            n_skips = n_skips - 1
        skip_length = round(math.sqrt(self.length), 0)
        #print("self.length:", self.length, " n_skips :", n_skips, " skip_length:", skip_length)
        """ Write logic to add skip pointers to the linked list. 
            This function does not return anything.
            To be implemented."""
        # test successfully
        pos = self.start_node
        m = self.start_node

        for _ in range(n_skips):
            for _ in range(int(skip_length)):
                pos = pos.next
            m.skip = pos
            m = m.skip
        return



    def insert_at_end(self, value, score):
        """ Write logic to add new elements to the linked list.
            Insert  the element at an appropriate position, such that elements to the left are lower than the inserted
            element, and elements to the right are greater than the inserted element.
            To be implemented. """
        # test successfully
        # if value not in self.traverse_list():
        new_node = Node(value=value, tfidf=score)
        pos = self.start_node

        if self.start_node is None:
            self.start_node = new_node
            self.end_node = new_node
            self.length += 1
            return

        else:
            test_now = self.traverse_list()
            if value not in test_now:
                self.length += 1
                if self.start_node.value > value:
                    self.start_node = new_node
                    self.start_node.next = pos
                    return

                elif self.end_node.value < value:
                    self.end_node.next = new_node
                    self.end_node = new_node
                    return

                else:
                    while pos.value < value < self.end_node.value and pos.next is not None:
                        pos = pos.next

                    m = self.start_node
                    while m.next != pos and m.next is not None:
                        m = m.next

                    m.next = new_node
                    new_node.next = pos
                    return

    # def sort_at_end(self, value, score):   # used
    #     """ Write logic to add new elements to the linked list.
    #         Insert  the element at an appropriate position, such that elements to the left are lower than the inserted
    #         element, and elements to the right are greater than the inserted element.
    #         To be implemented. """
    #     # test successfully
    #     # if value not in self.traverse_list():
    #     new_node = Node(value=value, tfidf=score)
    #     pos1 = self.start_node
    #
    #     if self.start_node is None:
    #         self.start_node = new_node
    #         self.end_node = new_node
    #         self.length += 1
    #         return
    #
    #     else:
    #         test_now = self.traverse_list()
    #         print("test_now", test_now)
    #         if value not in test_now:
    #             self.length += 1
    #             if self.start_node.tfidf > score:
    #                 self.start_node = new_node
    #                 self.start_node.next = pos1
    #                 return
    #
    #             elif self.end_node.tfidf < score:
    #                 self.end_node.next = new_node
    #                 self.end_node = new_node
    #                 return
    #
    #             else:
    #                 while pos1.tfidf < score < self.end_node.tfidf and pos1.next is not None:
    #                     pos1 = pos1.next
    #
    #                 m = self.start_node
    #                 while m.next != pos1 and m.next is not None:
    #                     m = m.next
    #
    #                 m.next = new_node
    #                 new_node.next = pos1
    #                 return


# test code part
# linked_list = LinkedList()
# linked_list.sort_at_end(33,10)
# linked_list.sort_at_end(83,0.7)
# linked_list.sort_at_end(33,1)
# linked_list.sort_at_end(43,1)
# print(linked_list.traverse_list())
# # #
# #[linked_list.insert_at_end(i,j) for i in [42, 111, 14, 29, 7, -11, 19, 13, 25, 10] for j in [4.2, 11.1, 1.4, 2.9, 0.7, -1.1, 1.9, 1.3, 2.5, 1.0]]
# #[linked_list.sorted_at_end(i,j) for i in [42, 111, 14, 29, 7, -11, 19, 13, 25, 10] for j in [4.2, 11.1, 1.4, 2.9, 0.7, -1.1, 1.9, 1.3, 2.5, 1.0]]
# [linked_list.sorted_at_end(i,j) for i in [42, 111] for j in [2.4, 4,3]]
# #print(linked_list.insert_at_end(33,0))
# #print(linked_list.sorted_at_end(33,0))
# #linked_list.insert_at_end(33,0)
# # linked_list.sorted_at_end(33,0)
# # linked_list.sorted_at_end(23,0.7)
# # linked_list.sorted_at_end(53,0.9)
# print(linked_list.traverse_list())
# # # print(linked_list)
# print(linked_list.traverse_list())
# print(linked_list.length)
# print(linked_list.add_skip_connections())
# print(linked_list.traverse_skips())
# #print(linked_list.start_node, linked_list.end_node)


