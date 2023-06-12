#!/usr/bin/env python3
def no_c(my_string):
    translation_table = str.maketrans("", "", "cC")
    translated_text = my_string.translate(translation_table)
    return translated_text
