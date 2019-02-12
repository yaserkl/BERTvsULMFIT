## Instructions

## 1. Requirements

* CUDA 9.0
* Python 3.6
* pip install -r requirements.txt

Run [download.sh](download.sh) to download the datasets.

Run [prepare_datasets.py](prepare_datasets.py) notebook to prepare the datasets.

## 2. Results

### 2.1 BERT

Bert                       | F1-score | Precision | Recall | Accuracy | Error Rate
-------------------------- | :------: | :-------: | :----: | :------: | :--------:
20ng                       |   91.24  |   91.46   |  91.13 |   91.04  |    8.96
IMDB                       |   88.59  |   88.61   |  88.62 |   88.6   |    11.4
Reuters 21578 (R8)         |   94.38  |   93.62   |  95.64 |   98.12  |    1.88
Reuters 21578 (R52)        |   73.80  |   73.48   |  76.01 |   96.35  |    3.65
Ohsumed (all docs)         |   70.45  |   73.97   |  68.84 |   79.30  |    20.70
Ohsumed (first 20k docs)   |   56.52  |   61.49   |  56.04 |   71.04  |    28.96


### 2.2 ULMFit

ULMFit                     | F1-score | Precision | Recall | Accuracy
-------------------------- | :------: | :-------: | :----: | :------:
20ng                       |   0.91   |   0.915   |  0.911 |   0.91
IMDB                       | 86.0     | 91.7      |        |
Reuters 21578 (R8)         | **85.1** | **91.8**  |        |
Reuters 21578 (R52)        | **85.1** | **91.8**  |        |
Ohsumed (all docs)         | 83.5     | 90.1      |        |
Ohsumed (first 20k docs)   | 83.5     | 90.1      |        |
