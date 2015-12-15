#!/usr/bin/env python
# coding=utf-8
"""
Annotate module
"""
from __future__ import unicode_literals
from __future__ import absolute_import

__author__ = "Clare Corthell"
__copyright__ = "Copyright 2015, summer.ai"
__date__ = "2015-12-07"
__email__ = "clare@summer.ai"

from textblob import TextBlob
from nltk.tokenize import sent_tokenize
import re


def get_snippets(word, doc):
    """
    Given word and doc
    Returns any snippets from doc containing word

    NB: Does not always properly deal with em-dashes (u'\u2014')

    """
    locations = [m.start() for m in re.finditer(word, doc)]

    snippets = []

    for loc in locations:
        start = loc - 200  # if > 200?
        end = loc + len(word) + 200  # this too
        tokenized = sent_tokenize(doc[start:end])
        for i in tokenized:
            if i.lower().find(word.lower()) > -1:
                snippets.append(i)

    return snippets


def find_word(doc, word):
    """
    Given (doc, word)
    Returns sentences containing word and position

    """
    sentence = doc
    positions = [i for i, x in enumerate(sentence.split()) if x == word]
    position = positions[0] or None
    return sentence, position


def annotate_sentence(doc, sentence):
    """
    Given (doc, sentence)

    Stripped of all punctuation & accents, lower case, target term replaced with _TERM_
    Tokenised and POS-Tagged (Penn Treebank)
    Single feature marker for sentences, such as number of sub-clauses (os something that actually makes sense)
    
    Returns
    {   "s":         ...,
        "s_clean":   ...,
        "pos_tags": ...,
        "pos":       ...,
        "features":  ...  }

    """
    blob = TextBlob(sentence)
    pos = blob.pos_tags

    pos_tags = ['/'.join([b[0], b[1]]) for b in pos]
    pos = list(pos_tags)
    pos[position] = '_TERM_'

    structured = {
        's': sentence,  # need to extract the sentence
        's_clean': sentence.replace(word, '_TERM_'),
        'pos_tags': ' '.join(pos_tags),
        'pos': pos,
        'features': None
    }
    return structured


def annotate_document(doc, word):
    """
    Given (doc, word)

    get sentence with word
    Stripped of all punctuation & accents, lower case, target term replaced with _TERM_
    Tokenised and POS-Tagged (Penn Treebank)
    Single feature marker for sentences, such as number of sub-clauses (os something that actually makes sense)
    
    Returns
    {   "s":         ...,
        "s_clean":   ...,
        "pos_tags": ...,
        "pos":       ...,
        "features":  ...  }
    """
    sentence, position = find_word(doc, word)
    blob = TextBlob(sentence)
    pos = blob.pos_tags

    pos_tags = ['/'.join([b[0], b[1]]) for b in pos]
    pos = list(pos_tags)
    pos[position] = '_TERM_'

    structured = {
        's': sentence,  # need to extract the sentence
        's_clean': sentence.replace(word, '_TERM_'),
        'pos_tags': ' '.join(pos_tags),
        'pos': pos,
        'features': None
    }
    return structured
