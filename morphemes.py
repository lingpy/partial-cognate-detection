"""
Script counts number of morphemes per noun in the data of Wang, used in Hamed
and Wang (2006)
"""
from __future__ import print_function, division
from util import pcd_path
from lingpy import *
wl = Wordlist(pcd_path('data', 'Wang-2006-200-23.tsv'))

nouns = {}
words = {}
all_nouns = 0
all_words = 0
for k in wl:
    if wl[k,'pos'] == 'n':
        try:
            nouns[len(wl[k,'partial'])] += 1
        except KeyError:
            nouns[len(wl[k,'partial'])] = 1
        all_nouns += 1
    try:
        words[len(wl[k,'partial'])] += 1
    except KeyError:
        words[len(wl[k,'partial'])] = 1
    all_words += 1

for i in range(1,len(nouns)+1):
    print('Nouns consisting of {0} morpheme(s)'.format(i), 
            '{0:.4f}'.format(nouns[i] / all_nouns))
print("")
for i in range(1,len(words)+1):
    print('Words consisting of {0} morpheme(s)'.format(i), 
            '{0:.4f}'.format(words[i] / all_words))
