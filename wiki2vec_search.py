import gzip
from pathlib import Path
import json
import sys
from wikipedia2vec import Wikipedia2Vec


def main(query, count):
    wiki2vec = Wikipedia2Vec.load("models/jawiki_20180420_100d.pkl")
    words = wiki2vec.most_similar(wiki2vec.get_word(query), count)
    for word, score in words:
        print(f"{word}\t{score}")


query = sys.argv[1]
count = int(sys.argv[2])
main(query, count)
