## Instructions

### 1. Requirements

* CUDA 9.0
* Python 3.6
* pip install -r requirements.txt

Run [download.sh](download.sh) to download the datasets.

Run [prepare_datasets.py](prepare_datasets.py) notebook to prepare the datasets.

### 2. Results

## 2.1 BERT

Bert                       | F1-score | Precision | Recall | Accuracy
-------------------------- | :------: | :-------: | :----: | :------:
20ng                       |   0.91   |   0.915   |  0.911 |   0.91
IMDB                       | 86.0     | 91.7      |        |
Reuters 21578 (R8)         | **85.1** | **91.8**  |        |
Reuters 21578 (R52)        | **85.1** | **91.8**  |        |
Ohsumed (all docs)         | 83.5     | 90.1      |        |
Ohsumed (first 20k docs)   | 83.5     | 90.1      |        |


## 2.2 ULMFit

ULMFit                     | F1-score | Precision | Recall | Accuracy
-------------------------- | :------: | :-------: | :----: | :------:
20ng                       |   0.91   |   0.915   |  0.911 |   0.91
IMDB                       | 86.0     | 91.7      |        |
Reuters 21578 (R8)         | **85.1** | **91.8**  |        |
Reuters 21578 (R52)        | **85.1** | **91.8**  |        |
Ohsumed (all docs)         | 83.5     | 90.1      |        |
Ohsumed (first 20k docs)   | 83.5     | 90.1      |        |
