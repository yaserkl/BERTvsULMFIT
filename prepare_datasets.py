from utils import *
from os.path import expanduser

deep_cleaning = False # basic cleaning
HOME = expanduser("~")

datasets = ['20ng', 'r8', 'r52', 'ohsumed_all', 'ohsumed_first', 'imdb']

for dataset in datasets:
    if dataset == '20ng':
        parser = download_20ng()
    elif dataset == 'r8':
        parser = parse_reuters('{}/data/r8/r8-train-all-terms.txt'.format(HOME),
                             '{}/data/r8/r8-test-all-terms.txt'.format(HOME))
    elif dataset == 'r52':
        parser = parse_reuters('{}/data/r52/r52-train-all-terms.txt'.format(HOME),
                               '{}/data/r52/r52-test-all-terms.txt'.format(HOME))
    elif dataset == 'ohsumed_all':
        parser = parse_ohsumed_all('{}/data/ohsumed/ohsumed-all'.format(HOME))
    elif dataset == 'ohsumed_first':
        parser = parse_ohsumed_first('{}/data/ohsumed/ohsumed-first-20000-docs/training'.format(HOME),
                              '{}/data/ohsumed/ohsumed-first-20000-docs/test'.format(HOME))
    elif dataset == 'imdb':
        parser = parse_imdb('{}/data/imdb/v1/aclImdb/train'.format(HOME), 
                            '{}/data/imdb/v1/aclImdb/test'.format(HOME))
    data_dir = "{}/working_dir/classification/files/{}/".format(HOME, dataset)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    prep_data(data_dir, parser, cleaning_doc=deep_cleaning)
    print("Dataset {} is prepared and stored in {}".format(dataset, data_dir))