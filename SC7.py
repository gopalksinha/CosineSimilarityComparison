# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:24:55 2019

@author: E0377413
"""



doc_candidate = ["Gopal", "Sagar" , "Sanjay", "Kaushik"]
doc_cosine = [2,9,4,1]
sort_cosine = doc_cosine.copy()
sort_cosine.sort(reverse=True)

for  i in sort_cosine:
 sort_index = doc_cosine.index(i)
 #print(i, ' = ', sort_index)
 print(sort_cosine[sort_index],'-----',doc_candidate[sort_index])
 
 
 
