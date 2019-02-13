#!/usr/bin/env bash

r8_out=$HOME/data/r8
r52_out=$HOME/data/r52
ohsumed_out=$HOME/data/ohsumed/
imdb_out=$HOME/data/imdb/

mkdir -p $r8_out
mkdir -p $r52_out
mkdir -p $ohsumed_out
mkdir -p $imdb_out
current=$(pwd)

cd $r8_out
wget https://www.cs.umb.edu/~smimarog/textmining/datasets/r8-train-all-terms.txt
wget https://www.cs.umb.edu/~smimarog/textmining/datasets/r8-test-all-terms.txt

cd $r52_out
wget https://www.cs.umb.edu/~smimarog/textmining/datasets/r52-train-all-terms.txt
wget https://www.cs.umb.edu/~smimarog/textmining/datasets/r52-test-all-terms.txt

cd $ohsumed_out
wget http://disi.unitn.it/moschitti/corpora/ohsumed-all-docs.tar.gz
tar xvfz ohsumed-all-docs.tar.gz
wget http://disi.unitn.it/moschitti/corpora/ohsumed-first-20000-docs.tar.gz
tar xvfz ohsumed-first-20000-docs.tar.gz

cd $imdb_out
wget http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
tar xvfz aclImdb_v1.tar.gz

cd $current

pip install -r requirements.txt

#conda install gxx_linux-64

cd ulmfit
unzip fastai-0.7.0.zip
cd fastai-0.7.0
python setup.py install
rm -rf fastai-0.7.0
cd $current

python -m spacy download en

# install phantomjs for plotting
# sudo npm install -g phantomjs-prebuilt
# alternative option for user:

wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2
cd phantomjs-2.1.1-linux-x86_64

export BOKEH_PHANTOMJS_PATH=$(pwd)/bin/phantomjs
export PATH=$(pwd)/bin:$PATH

cd ..
rm phantomjs-2.1.1-linux-x86_64.tar.bz2

cd $current