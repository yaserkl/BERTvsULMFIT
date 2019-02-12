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