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
mamba create -n ai-1 python=3.6
conda activate ai-1
pip install opencv-python==3.3.1.11
```
3. start spyder by typing `spyder` and open `iso-cv-scanner.py`

## 2 - phenopype

1. create new virtual environment
```
mamba create -n ai-2 python=3.7
conda activate ai-2
pip install phenopype
pip install jupyter notebook
```
2. dowload tutorials: https://github.com/phenopype/phenopype-tutorials/archive/refs/heads/main.zip
3. start `jupyter notebook` and run tutorials 
4. download https://github.com/phenopype/phenopype-gallery/archive/refs/heads/main.zip
5. start `jupyter notebook` and run the vignettes 
6. (optional) do all this in spyder (needs to be installed first)

## 3 - use pretrained model to segment damselflies



## 4 - segment anything algorthim

1. go to https://colab.research.google.com/github/facebookresearch/segment-anything/blob/main/notebooks/predictor_example.ipynb
2. select 'GPU' under 'Edit'>'Notebook Settings'->'Hardware accelerator'
3. select "Edit" > "Clear all outputs" (avoids spoilers)
4. run code cell by cell
