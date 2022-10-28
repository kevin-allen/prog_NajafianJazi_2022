# prog_NajafianJazi_2022
Code used in a manuscript by Najafian Jazi and colleagues



### Python Environment

I installed the default Anaconda.
Make sure conda has access to the internet if behind a proxy.
Get Deeplabcut source code: git clone https://github.com/DeepLabCut/DeepLabCut.git
Install the DEEPLABCUT conda environment: conda env create -f DEEPLABCUT.yaml. I remove the [gui] from the DEEPLABCUT.yaml file and added seaborn.
conda activate DEEPLABCUT
echo "conda activate DEEPLABCUT" >> ~/.bashrc
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=DEEPLABCUT
conda install Cython
conda install -c conda-forge jupyterlab
Install spikeA (don't install dependency, use conda to install them if needed)
Install autopipy
Install positrack2
