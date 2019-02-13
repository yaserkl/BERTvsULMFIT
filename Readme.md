## Instructions

\[THIS REPOSITORY IS UNDER DEVELOPMENT AND MOER DATASETS AND MODELS WILL BE ADDED\]

\[FEEL FREE TO MAKE PULL REQUEST FOR A NEW DATASET OR NEW MODEL\]

## 1. Requirements

* CUDA 9.0
* Python 3.6
* `bash setup.sh`


Run [setup.sh](setup.sh) to download the datasets and install all the required packages.

Run [prepare_datasets.py](prepare_datasets.py) notebook to prepare the datasets.

For instruction regarding running each model go the respective model directory.

The [models](models) directory holds the result of these experiments.


![alt text](https://github.com/yaserkl/BERTvsULMFIT/raw/master/models/bert/20ng/cm_20ng.png)
![alt text](https://github.com/yaserkl/BERTvsULMFIT/raw/master/models/bert/20ng/sankey_20ng.png)


## 2. Results

### 2.1 BERT

Bert (MXNet)               | F1-score | Precision | Recall  | Accuracy | Error Rate
-------------------------- | :------: | :-------: | :----:  | :------: | :--------:
20ng                       |   91.24  |   91.46   |  91.13  |   91.04  |    8.96
IMDB                       |   88.59  |   88.61   |  88.62  |   88.6   |    11.4
Reuters 21578 (R8)         |   94.38  |   93.62   |  95.64  |   98.12  |    1.88
Reuters 21578 (R52)        | **73.80**|   73.48   |**76.01**|   96.35  |    3.65
Ohsumed (all docs)         |   70.45  |   73.97   |  68.84  |   79.30  |    20.70
Ohsumed (first 20k docs)   | **56.52**| **61.49** |**56.04**| **71.04**|  **28.96**


### 2.2 ULMFit

ULMFit                     | F1-score | Precision | Recall  | Accuracy | Error Rate
-------------------------- | :------: | :-------: | :----:  | :------: | :--------:
20ng                       | **92.87**| **93.02** |**92.82**| **92.82**|  **7.18**
IMDB                       |**91.92** | **91.96** |**91.96**| **91.92**|  **8.08**
Reuters 21578 (R8)         | **94.79**| **94.07** |**96.12**| **98.18**|  **1.82**
Reuters 21578 (R52)        |   73.77  | **75.47** |  75.96  | **96.43**|  **3.57**
Ohsumed (all docs)         |**74.82** | **75.01** |**75.47**| **81.96**|  **18.04**
Ohsumed (first 20k docs)   |   43.76  |   44.46   |  45.49  |   62.5   |    37.5
