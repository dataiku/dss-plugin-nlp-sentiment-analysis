# -*- coding: utf-8 -*-
import re
import string
import six


# Twitter related tokens
RE_HASHTAG = u"#[a-zA-Z0-9_]+"
RE_MENTION = u"@[a-zA-Z0-9_]+"

RE_URL = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
RE_EMAIL = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""  # noqa


TOKENS_TO_IGNORE = [RE_HASHTAG, RE_EMAIL, RE_MENTION, RE_URL]


def clean_text(text):
    """
    Applies some pre-processing to clean text data.

    In particular:
    - lowers the string
    - removes URLs, e-mail adresses
    - removes Twitter mentions and hastags
    - removes HTML tags
    - removes the character [']
    - replaces punctuation with spaces

    """

    text = text.lower()  # lower text

    # ignore urls, mails, twitter mentions and hashtags
    for regex in TOKENS_TO_IGNORE:
        text = re.sub(regex, "", text)

    text = re.sub(r"<[^>]*>", "", text)  # remove HTML tags if any

    # remove the character [']
    text = re.sub(r"\'", " ", text)

    # this is the default cleaning in Keras,
    # it consists in lowering the texts and removing the punctuation
    filters = u'!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'

    split = u" "  # character that will be used to split the texts later

    if isinstance(text, six.text_type):
        translate_map = dict((ord(c), split) for c in filters)
        text = text.translate(translate_map)
    elif len(split) == 1:
        translate_map = (
            string.maketrans(filters, split * len(filters)) if six.PY2 else str.maketrans(filters, split * len(filters))
        )
        text = text.translate(translate_map)
    else:
        for c in filters:
            text = text.replace(c, split)

    cleaned_text = " ".join(text.split()).strip()
    return cleaned_text
