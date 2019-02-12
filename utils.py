import os
import re
import nltk
import csv
from collections import Counter, defaultdict
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups
from glob import glob
import pandas as pd
import numpy as np
np.random.seed(123)

stop_words = set(stopwords.words('english'))

# download datasets from: http://disi.unitn.it/moschitti/corpora.htm
def one_hot(x, num):
    one_hot = np.zeros((len(x), num))
    one_hot[np.arange(len(x)), x] = 1
    return one_hot


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def clean_doc(x, word_freq):
    clean_docs = []
    most_commons = dict(word_freq.most_common(min(len(word_freq), 50000)))
    for doc_content in x:
        doc_words = []
        cleaned = clean_str(doc_content.strip())
        for word in cleaned.split():
            if word not in stop_words and word_freq[word] >= 5:
                if word in most_commons:
                    doc_words.append(word)
                else:
                    doc_words.append("<UNK>")
        doc_str = ' '.join(doc_words).strip()
        clean_docs.append(doc_str)
    return clean_docs


def download_20ng():
    #categories = ["comp.graphics", "sci.space", "rec.sport.baseball"]
    # newsgroups_train = fetch_20newsgroups(subset='train', remove=("headers", "footers", "quotes"))#, categories=categories)
    # newsgroups_test = fetch_20newsgroups(subset='test', remove=("headers", "footers", "quotes"))#, categories=categories)

    newsgroups_train = fetch_20newsgroups(subset='train')
    newsgroups_test = fetch_20newsgroups(subset='test')

    return newsgroups_train.data, newsgroups_train.target, newsgroups_test.data, newsgroups_test.target


def parse_reuters(train_file, test_file):
    ### get training/test file from here: https://www.cs.umb.edu/~smimarog/textmining/datasets/
    def reader(path):
        lines = open(path).readlines()
        texts = []
        labels = []
        for _ in lines:
            label, text = _.strip().split('\t')
            texts.append(text)
            labels.append(label)
        return texts, labels
    x_train, y_train = reader(train_file)

    uniques = np.unique(y_train)
    ids = np.arange(len(uniques))
    mapping = {_u:_i for _i, _u in zip(ids, uniques)}
    y_train = [mapping[_l] for _l in y_train]

    x_test, y_test = reader(test_file)
    y_test = [mapping[_l] for _l in y_test]
    return x_train, y_train, x_test, y_test


def ohsumed_reader(data_dir):
    file_category = defaultdict(list)
    for _dir in glob('{}/*'.format(data_dir)):
        category = _dir.split('/')[-1]
        for _file in glob('{}/*'.format(_dir)):
            _file_name = _file.split('/')[-1]
            file_category[_file_name].append(category)

    filtered_filenames = [k for k, v in file_category.items() if len(v) == 1]
    texts = []
    labels = []
    for _dir in glob('{}/*'.format(data_dir)):
        category = _dir.split('/')[-1]
        for _file in glob('{}/*'.format(_dir)):
            _file_name = _file.split('/')[-1]
            if _file_name in filtered_filenames:
                texts.append(open(_file).read().strip())
                labels.append(category)
    uniques = np.unique(labels)
    ids = np.arange(len(uniques))
    mapping = {_u: _i for _i, _u in zip(ids, uniques)}
    labels = [mapping[_l] for _l in labels]
    return texts, labels


def parse_ohsumed_all(data_dir):
    # download files from: http://disi.unitn.it/moschitti/corpora/ohsumed-all-docs.tar.gz
    texts, labels = ohsumed_reader(data_dir)
    x_train, x_test, y_train, y_test = train_test_split(texts, labels, test_size=0.15, random_state=1)

    return x_train, y_train, x_test, y_test


def parse_ohsumed_first(train_dir, test_dir):
    # download files from: http://disi.unitn.it/moschitti/corpora/ohsumed-first-20000-docs.tar.gz

    x_train, y_train = ohsumed_reader(train_dir)
    x_test, y_test = ohsumed_reader(test_dir)

    return x_train, y_train, x_test, y_test


def parse_imdb(train_dir, test_dir):
    # download files from: http://ai.stanford.edu/~amaas/data/sentiment/
    def reader(data_dir):
        texts = []
        labels = []
        for _file in glob('{}/pos/*'.format(data_dir)):
            texts.append(open(_file).read().strip())
            labels.append(1)
        for _file in glob('{}/neg/*'.format(data_dir)):
            texts.append(open(_file).read().strip())
            labels.append(0)
        # mix the positives and negatives
        perm = np.arange(len(texts))
        perm = np.random.permutation(perm)
        return np.array(texts)[perm], np.array(labels)[perm]

    x_train, y_train = reader(train_dir)
    x_test, y_test = reader(test_dir)
    return x_train, y_train, x_test, y_test


def to_csv(working_dir, X_train, X_val, X_test, y_train, y_val, y_test):
    ### for tsv files we put text as the first column
    train_dict = {'description': X_train, 'label': y_train}
    val_dict = {'description': X_val, 'label': y_val}
    test_dict = {'description': X_test, 'label': y_test}
    train_pd = pd.DataFrame.from_dict(train_dict)
    val_pd = pd.DataFrame.from_dict(val_dict)
    test_pd = pd.DataFrame.from_dict(test_dict)
    train_pd.to_csv('{}/train.tsv'.format(working_dir), index=False, sep='\t', header=False, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")
    val_pd.to_csv('{}/dev.tsv'.format(working_dir), index=False, sep='\t', header=False, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")
    val_pd.to_csv('{}/val.tsv'.format(working_dir), index=False, sep='\t', header=False, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")
    test_pd.to_csv('{}/test.tsv'.format(working_dir), index=False, sep='\t', header=False, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")

    ### for csv files we put label as the first column
    train_dict = {'text': X_train, 'label': y_train}
    val_dict = {'text': X_val, 'label': y_val}
    test_dict = {'text': X_test, 'label': y_test}
    train_pd = pd.DataFrame.from_dict(train_dict)
    val_pd = pd.DataFrame.from_dict(val_dict)
    test_pd = pd.DataFrame.from_dict(test_dict)
    train_pd.to_csv('{}/train.csv'.format(working_dir), index=False, sep=',', header=False, quoting=csv.QUOTE_NONE,
                    quotechar="", escapechar="\\")
    val_pd.to_csv('{}/dev.csv'.format(working_dir), index=False, sep=',', header=False, quoting=csv.QUOTE_NONE,
                  quotechar="", escapechar="\\")
    val_pd.to_csv('{}/val.csv'.format(working_dir), index=False, sep=',', header=False, quoting=csv.QUOTE_NONE,
                  quotechar="", escapechar="\\")
    test_pd.to_csv('{}/test.csv'.format(working_dir), index=False, sep=',', header=False, quoting=csv.QUOTE_NONE,
                   quotechar="", escapechar="\\")


def prep_data(working_dir, parser, cleaning_doc=True):
    if not os.path.exists(working_dir):
        os.makedirs(working_dir)

    X_train, y_train, X_test, y_test = parser

    word_freq = Counter()  # to remove rare words
    for text in X_train:
        for word in clean_str(text.strip()).split():
        #for word in nltk.word_tokenize(text.lower()):
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    if cleaning_doc:
        X_train = clean_doc(X_train, word_freq)
        X_test = clean_doc(X_test, word_freq)
    else: # basic cleaning
        X_train = [clean_str(_) for _ in X_train]
        X_test = [clean_str(_) for _ in X_test]

    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.15, random_state=1)

    to_csv(working_dir, X_train, X_val, X_test, y_train, y_val, y_test)
