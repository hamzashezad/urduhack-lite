# coding: utf8
"""
Tokenization
==============

This module is another crucial part of the Urduhack. This module performs tokenization on sentence. It separates
different sentence from each other and converts each string into a complete **sentence token**. Note here you must not
confuse yourself with the word token. They are two completely different things.

The tokenization of Urdu text is necessary to make it useful for the NLP tasks.
This module provides the following functionality:

    - Sentence Tokenization

The tokenization of Urdu text is necessary to make it useful for the machine
learning tasks. In the :py:mod:`~urduhack.tokenization` module, we solved the problem related to
sentence tokenization.
"""
from .tokenizer import sentence_tokenizer

__all__ = ["sentence_tokenizer"]