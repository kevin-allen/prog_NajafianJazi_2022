# prog_NajafianJazi_2022

Code used in a manuscript by Najafian Jazi and colleagues.

The starting point for the analysis is in the `main.ipynb` located in the `behavior_only` and `electrophys_behavior` directories.


## Python Environment

1. I installed the default [Anaconda](https://www.anaconda.com/).
2. Make sure conda has access to the internet if behind a proxy.
3. Get Deeplabcut source code: `git clone https://github.com/DeepLabCut/DeepLabCut.git`
4. Install the DEEPLABCUT conda environment: `conda env create -f DEEPLABCUT.yaml`. I remove the `[gui]` from the DEEPLABCUT.yaml file and added seaborn.
6. `conda activate DEEPLABCUT`
7. `echo "conda activate DEEPLABCUT" >> ~/.bashrc`
8. `conda install -c anaconda ipykernel`
9. `python -m ipykernel install --user --name=DEEPLABCUT`
10. `conda install Cython`
12. `conda install -c conda-forge jupyterlab`
13. Install spikeA (don't install dependency, use conda to install them if needed)
14. Install autopipy
15. Install positrack2
