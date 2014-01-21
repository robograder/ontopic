"""
defines function to extract keywords from prompt
"""
import sys

import nltk

from nltk.corpus import brown as brown_corpus
from nltk.corpus import wordnet


def die_nltk_data_error(corpus):
    sys.stderr.write("Missing nltk data (%s). User install_nltk_data.sh script\n" % corpus)
    sys.exit(1)

try:
    brown_corpus.words()
except LookupError:
    die_nltk_data_error('brown')

try:
    wordnet.get_version()
except LookupError:
    die_nltk_data_error('wordnet')

def extract_keywords(prompt):
    tokens = nltk.word_tokenize(prompt)
    # build the brown freq dist - slow!
    fd = nltk.FreqDist(brown_corpus.words())

    # decorate sort undecorate with freq
    tokens_with_freq = [(fd.freq(t), t) for t in tokens]
    for _, t in sorted(tokens_with_freq):
        print t




if __name__ == "__main__":
    print extract_keywords(sys.argv[1])


