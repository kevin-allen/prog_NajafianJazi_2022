"""
This files sets my working environment to work with this project.

It imports some packages that I often use, creates list of recording session (autopipy and spikeA).

I also added some useful functions that I use when processing data

Simply put %run setup_project.py in a jupyter notebook to run the code
"""
import pandas as pd
import numpy as np
import os.path
import shutil
import pickle
from tqdm import tqdm
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from itertools import compress
import socket


from autopipy.project import Project # a for autopipy
from autopipy.session import Session # a for autopipy
from autopipy.trialElectro import TrialElectro # a for autopipy

from spikeA.Session import Kilosort_session
from spikeA.Session import Tetrode_session
from spikeA.Animal_pose import Animal_pose
from spikeA.Spike_train_loader import Spike_train_loader
from spikeA.Cell_group import Cell_group
from spikeA.Dat_file_reader import Dat_file_reader

projectName="autopi_ca1"
dataPath="/adata/projects/autopi_ca1"
dlcModelPath="/adata/models"
myProject = Project(name=projectName,dataPath=dataPath,dlcModelPath=dlcModelPath)
fn=myProject.dataPath+"/newSessions"
print("Reading " + fn)
sessionNames = pd.read_csv(fn) # this will be a pandas dataframe
print("We have {} testing sessions in the list".format(len(sessionNames)))
myProject.createSessionList(sessionNameList=sessionNames.sessionName.to_list()) 
sSesList = [Kilosort_session(ses.name,ses.path) for ses in myProject.sessionList]
print("See myProject and sSesList objects")


def load_parameters_from_files_project(sSesList):
    for ses in tqdm(sSesList):
        ses.load_parameters_from_files()

def load_spike_train_project(sSesList):    
    for ses in tqdm(sSesList):
        ses.load_parameters_from_files()
        stl = Spike_train_loader()
        ses.stl= stl
        stl.load_spike_train_kilosort(ses)
        ses.cg = Cell_group(stl)
    

def data_location(sSesList):
    """
    Arguments:
    sSesList: list of spikeA sessions
    
    returns a dataframe with session, mouse, hd, ip columns for all sessions of the sSesList
    """
    res = [ session_data_location(sSes) for sSes in sSesList]
    df = pd.DataFrame({"session": [ s for s,m,h,ip in res],
                 "mouse": [ m for s,m,h,ip in res],
                  "hd": [ h for s,m,h,ip in res],
                  "ip": [ ip for s,m,h,ip in res]})    
    return df
def session_data_location(sSes):
    """
    Find on which hard drive and computer (ip) the data are located
    """
    mouse_dir,session = os.path.split(sSes.path)
    first_level = os.readlink(mouse_dir)
    first_level =os.path.normpath(first_level)
    second_level = os.readlink(first_level)
    hd = second_level.split("/")[2]
    autom = pd.read_csv("/etc/auto.ext_drives",sep='\t', lineterminator='\n',header=None)
    autom.columns = ["hd","param","ip"]
    ip = autom.loc[autom.hd==hd].ip.item().split(":")[0].split(".")[0]
    return sSes.name,sSes.subject,hd,ip

def get_local_indices(dat_loc,ip=None):
    """
    returns a numpy array of boolean, whether sessions are on a specific computer
    """
    return (dat_loc.ip==ip).to_numpy()

def get_local_sessions(sSesList,ip=None):
    """
    Get a list of sessions that are local to the computer running this code
    
    If ip is left to None, it will get the local ip for you
    """
    if ip is None:
        ip=socket.gethostname()
    dat_loc =data_location(sSesList)
    i = get_local_indices(dat_loc,ip)
    return list(compress(sSesList, i))