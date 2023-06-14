#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        i = 1
        my_keys = []
        for key in a_dictionary:
            my_keys.append(key)
        temp = my_keys[0]
        while i < len(a_dictionary):
            if a_dictionary[my_keys[i]] > a_dictionary[temp]:
                temp = my_keys[i]
            i+=1
        return temp
    return None


