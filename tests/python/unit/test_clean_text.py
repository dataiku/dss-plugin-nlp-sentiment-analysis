# -*- coding: utf-8 -*-
# This is a test file intended to be used with pytest
# pytest automatically runs all the function starting with "test_"
# see https://docs.pytest.org for more information

from preprocessing_utils import clean_text

# - lowers the string
# - removes URLs, e-mail adresses
# - removes Twitter mentions and hastags
# - removes HTML tags
# - removes the character [']
# - replaces punctuation with spaces


def test_clean_web_text():
    original_text = u"<p>#THOUGHT envoie dictée à bernard@pivot.fr ou @bernard https://dictee.fr </p>"
    cleaned_text = clean_text(original_text)
    assert cleaned_text == u"envoie dictée à ou"


def test_clean_punctuation():
    original_text = u"""Bachibouzouk d'Oh !"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n"""
    cleaned_text = clean_text(original_text)
    assert cleaned_text == u"bachibouzouk d oh"
