import pandas as pd
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import time
import numpy as np

def possibilities(col1, col2):
    possibilities_dict = {}
    for a in col1:
        possibilities_dict[a] = list(col2)
    return possibilities_dict

def matcher(col1, col2):
    possibilities_dict = possibilities(col1, col2)
    matcher_dict = {}
    for i in possibilities_dict:
        ratio_list = []
        compere_list = []
        for j in possibilities_dict[i]:
            ratio = fuzz.ratio(i, j)
            ratio_list.append(ratio)
            compere_list.append((i, j))
        max_ratio_index = ratio_list.index(max(ratio_list))
        matcher_dict[compere_list[max_ratio_index]] = max(ratio_list)
    return matcher_dict

def compere_matcher(col1, col2, col_names):
    matcher_dict = matcher(col1, col2)
    compere_df = pd.DataFrame(columns=col_names)
    col1 = []
    col2 = []
    score = []
    for i in range(len(matcher_dict.keys())):
        col1.append(list(matcher_dict.keys())[i][0])
        col2.append(list(matcher_dict.keys())[i][1])
        score.append(list(matcher_dict.values())[i])
    compere_df[col_names[0]] = col1
    compere_df[col_names[1]] = col2
    compere_df[col_names[2]] = score
    return compere_df
