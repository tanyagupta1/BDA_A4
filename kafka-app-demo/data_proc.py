import os
import json
import json
import nltk
import pandas as pd
import string
import re
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
from string import punctuation

def return_input_data():
    punc=list(punctuation)
    d0 = json.load(open("A3_all_venues.json","r"))
    venues_authors={}
    for paper in d0.keys():
        venues_authors[paper]={}
        for venue in d0[paper]:
            v = venue.lower()
            v = v.translate(str.maketrans('', '', string.punctuation))
            v=re.sub("\s\s+", " ", v)
            v = v.replace(" ","_")
            v=v.strip()
            if (len(v)==0):
                v='_'
            venues_authors[paper][v]=d0[paper][venue]


    freqs={}
    for paper in venues_authors:
        for v in venues_authors[paper]:
            if v not in freqs.keys():
                freqs[v]=0
            freqs[v]+=1
    for_sort = [[v,k] for k,v in freqs.items()]
    for_sort = sorted(for_sort,reverse=True)
    selected_venues=[]
    for f,v in for_sort:
        selected_venues.append(v)
    selected_venues = selected_venues


    return venues_authors, selected_venues



    