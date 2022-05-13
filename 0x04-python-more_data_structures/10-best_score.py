#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list_key = list(a_dictionary.keys())
        list_value = list(a_dictionary.values())
        score = max(list_value)
        return(list_key[list_value.index(score)])
    return None
