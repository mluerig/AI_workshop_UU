# AI_workshop_UU

## 0 - how to use this repo

first, install mamba
```
conda install -c conda-forge mamba
```

## 1 - simple thresholding procedures for batch processing of isopods

1. download repo from https://github.com/mluerig/iso_cv
2. go to directory and make new virtual environment:

```
mamba create -n iso-cv-env python=3.6
conda activate iso-cv-env
pip install opencv-python==3.3.1.11
```
3. start spyder by typing `spyder` and open `iso-cv-scanner.py`

## 2 - phenopype

1. create new virtual environment
```
mamba create -n pp-env python=3.7
conda activate pp-env
pip install phenopype
pip install jupyter notebook
```
2. dowload tutorials: https://github.com/phenopype/phenopype-tutorials/archive/refs/heads/main.zip
3. start `jupyter notebook` and run tutorials 
4. download https://github.com/phenopype/phenopype-gallery/archive/refs/heads/main.zip
5. start `jupyter notebook` and run the vignettes 
6. (optional) do all this in spyder (needs to be installed first)

## 3 - use pretrained model to segment damselflies


[model was trained using Christophe Avenel's materials from the NBIS workshop on Deep Learning](https://github.com/NBISweden/workshop-neural-nets-and-deep-learning/blob/master/session_convolutionalNeuralNetworks/Labs/CNN_Keras_lab_2.ipynb)

1. in `pp-env`, install keras and tensorflow: `pip install keras tensorflow`  
2. download the project: https://drive.google.com/file/d/1tnE73y2mx3VjKzkfuiNXimZ8CPCE5EKr/view?usp=sharing
3. download the models: https://drive.google.com/drive/folders/1CEpkiKM14PX_iYfJ-ZPzWGYGoJC-9hpJ?usp=share_link
4. download this repo (https://github.com/mluerig/AI_workshop_UU/archive/refs/heads/main.zip) and open `scripts/01_phenopype_keras_model.py` in spyder
5. run the code - first the full body model, then body part specific segmentation 

## 4 - segment anything model (SAM)

1. go to https://segment-anything.com/demo and try some of the images we used so far
2. go to https://colab.research.google.com/github/facebookresearch/segment-anything/blob/main/notebooks/predictor_example.ipynb
3. select 'GPU' under 'Edit'>'Notebook Settings'->'Hardware accelerator'
4. select "Edit" > "Clear all outputs" (avoids spoilers)
5. run code cell by cell

## 5 - resources

https://github.com/NBISweden/workshop-neural-nets-and-deep-learning