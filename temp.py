import nltk
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
fhand=open("Hello.txt").read()
tokens=nltk.word_tokenize(fhand)
print(fhand)
print(tokens)

