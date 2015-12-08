#!/usr/bin/env python
# coding=utf-8
"""
Search module
"""
from __future__ import unicode_literals
from __future__ import absolute_import

__author__ = "Clare Corthell"
__copyright__ = "Copyright 2015, summer.ai"
__date__ = "2015-12-07"
__email__ = "clare@summer.ai"

from textblob import TextBlob


example = {
    "s": "A kalyptic culture is typified by peacefulness, tolerance and individualism.",
    "s_clean": "a _TERM_ culture is typified by peacefulness tolerance and individualism",
    "pos_tags": "A/DT _TERM_/JJ culture/NN is/VBZ typified/VBN by/IN peacefulness/NN ,/, tolerance/NN and/CC individualism/NN ./.",
    "features": {}
}


def find_word(text, word):
    """
    Given (text, word)
    Returns sentence containing word  TODO

    """
    return text


def structure_sentence(text, word):
    """
    Given (text, word)

    get sentence with word
    Stripped of all punctuation & accents, lower case, target term replaced with _TERM_
    Tokenised and POS-Tagged (Penn Treebank)
    Single feature marker for sentences, such as number of sub-clauses (os something that actually makes sense)
    
    Returns
    {   "s":        ...,
        "s_clean":  ...,
        "pos_tags": ...,
        "features": ...  }
    """
    sentence = find_word(text, word)

    blob = TextBlob(sentence)
    structured = {
        's': sentence,  # need to extract the sentence
        's_clean': sentence.replace(word, '_TERM_'),
        'pos_tags': ' '.join(['/'.join([b[0], b[1]]) for b in blob.pos_tags]),
        'features': None
    }
    return structured
