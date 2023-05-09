# AI_workshop_UU

![image](https://user-images.githubusercontent.com/15648068/236338994-2469c942-436a-4b54-aa04-8987c15918d8.png)

## [0] preparation

1. ~download and install anaconda (see https://www.phenopype.org/docs/installation/python/)~
1. download and install mambaforge: https://github.com/conda-forge/miniforge#mambaforge
2. after successfull installation (check by running `conda` in console), install mamba:
```
conda install -c conda-forge mamba
```
3. create a new conda environment, and activate it:
```
mamba create -n my-env python=3.7
mamba activate my-env
## if "mamba" doesn't work for activation, use "conda" instead
```
4. install "jupyter notebooks" and "spyder" using "mamba":
```
mamba install spyder jupyter notebook
```
5. install "phenopype" using "pip"
```
pip install phenopype
```
6. before continuing, a few notes about python environments:
 
 - be rigorous and ALWAYS make a new environment for a project
 - for each env all packages need to be re-installed, including python and spyder
 - dont't forget to activate your environment (check that it says `(my-env)` in the terminal, and not `(base)`)
 - see all your environments with `conda env list`

## [1] simple thresholding procedures for batch processing of isopods

**NOTE:** [iso-cv](https://github.com/mluerig/iso_cv) is a legacy repo with no real use other than demonstration of basic principles of computer vision. The workflow and functionality is fully contained in phenopype (www.phenopype.org), so please consider that when doing this tutorial - don't use it for production :grin: 

1. download repo https://github.com/mluerig/iso_cv/archive/refs/heads/master.zip (updated on 2023-05-09)
2. unpack, go to folder, open a terminal
3. activate the environment with `mamba activate my-env`
4. start spyder by typing `spyder` and open `iso-cv-scanner.py`
5. follow instructions

## [2] phenopype I - signal processing

**NOTE:** phenopype currently only works under windows / unix - sorry mac users. 

1. activate the environment with `mamba activate my-env`
2. dowload phenopoype tutorials: https://github.com/phenopype/phenopype-tutorials/archive/refs/heads/main.zip
3. start `jupyter notebook` and run tutorials 
4. download https://github.com/phenopype/phenopype-gallery/archive/refs/heads/main.zip
5. start `jupyter notebook` and run the vignettes 
6. (optional) do all this in spyder - e.g., save the notebooks as Python scripts from a running jupyter notebook using `File > Download as > Python (.py)`.

## [3] phenopype II - deep learning

**NOTE:** phenopype currently only works under windows / unix - sorry mac users. 

The DL model I use here was trained based on Christophe Avenel's [materials from the NBIS workshop on Deep Learning](https://github.com/NBISweden/workshop-neural-nets-and-deep-learning/blob/master/session_convolutionalNeuralNetworks/Labs/CNN_Keras_lab_2.ipynb) - see below 

1. in `pp-env`, install keras and tensorflow: `pip install keras tensorflow`  
2. download the project: https://drive.google.com/file/d/1tnE73y2mx3VjKzkfuiNXimZ8CPCE5EKr/view?usp=sharing
3. download the models: https://drive.google.com/drive/folders/1CEpkiKM14PX_iYfJ-ZPzWGYGoJC-9hpJ?usp=share_link
4. download this repo (https://github.com/mluerig/AI_workshop_UU/archive/refs/heads/main.zip) and open `scripts/01_phenopype_keras_model.py` in spyder
5. run the code - first the full body model, then body part specific segmentation 

## [4] segment anything model (SAM)

**NOTE:** I am currently working on implementing a SAM workflow in phenopype, please stay tuned or get in touch if you feel like you'd like to help me :grin:

1. try the interactive web-app - go to https://segment-anything.com/demo 
2. go to https://colab.research.google.com/github/facebookresearch/segment-anything/blob/main/notebooks/predictor_example.ipynb
3. select 'GPU' under 'Edit'>'Notebook Settings'->'Hardware accelerator'
4. select "Edit" > "Clear all outputs" (avoids spoilers)
5. run code cell by cell
6. try some of the images from the phenopype tutorials, or your own images

## [5] resources

- general CV terminology and introduction: https://www.frontiersin.org/articles/10.3389/fevo.2021.642774/full
- materials from NBIS workshop on DL (for self study) https://github.com/NBISweden/workshop-neural-nets-and-deep-learning
- napari image viewer in Python https://napari.org/stable/
- scientific community image forum (sponsored by the Center for Open Bioimage Analysis (COBA)) - https://forum.image.sc/. 
- mailing list for CV in ecology and evolution https://groups.google.com/g/cv-eeb-mail
