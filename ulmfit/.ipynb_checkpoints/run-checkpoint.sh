#!/usr/bin/env bash
#bash run.sh ~/working_dir/classification/files/imdb/ ~/working_dir/classification/models/ulmfit/imdb/ ~/working_dir/classification/files/wiki/en/ imdb

INDIR=$1
WORKDIR=$2
WIKIDIR=$3
NAME=$4

mkdir -p $WORKDIR

read -r -p "Download/Pre-train Wikipedia?: " choice
case "$choice" in
y|Y ) bash prepare_wiki.sh $HOME/data/classification/files/; python create_toks.py $WIKIDIR; python tok2id.py $WIKIDIR 50000 5; python pretrain_lm.py $WIKIDIR 0 --lr 1e-3 --cl 12 --bs 360;;
n|N ) echo "Skipping Pre-training on Wikipedia";;
* ) echo "Invalid answer"; exit 1;;
esac

#python create_toks.py --dir-path $INDIR --working-path $WORKDIR
#python tok2id.py --dir-path $WORKDIR 50000 5

#python finetune_lm.py --dir-path $WORKDIR --pretrain-path $WIKIDIR --cl 2 --bs 50 --lm-id pretrain_wiki --pretrain-id '' --cuda-id 0

#python train_clas.py --dir-path $WORKDIR --cuda-id 0 --lm-id pretrain_wiki --clas-id $NAME --cl 50

python eval_clas.py --dir-path $WORKDIR --cuda-id 0 --lm-id pretrain_wiki --clas-id $NAME