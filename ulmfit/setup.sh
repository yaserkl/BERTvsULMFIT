#!/usr/bin/env bash
#bash setup.sh ~/data/imdb/v1/ ~/data/wiki/en/ imdb_class

INDIR=$1
WIKIDIR=$2
NAME=$3

unzip fastai-0.7.0.zip
cd fastai-0.7.0
python setup.py install
cd ..

pip install spacy fire torch torchvision torchtext==0.2.3
python -m spacy download en

#bash prepare_wiki.sh $HOME/data/
#python create_toks.py $WIKIDIR
#python tok2id.py $WIKIDIR 50000 5

python create_toks.py $INDIR
python tok2id.py $INDIR 50000 5

#python pretrain_lm.py $WIKIDIR 0 --lr 1e-3 --cl 12 --bs 360

python finetune_lm.py $INDIR $WIKIDIR 1 25 --lm-id pretrain_wiki --pretrain-id '' --cuda-id 0

python train_clas.py $INDIR --cuda-id 0 --lm-id pretrain_wiki --clas-id $NAME --cl 50

python eval_clas.py $INDIR --cuda-id 0 --lm-id pretrain_wiki --clas-id $NAME
