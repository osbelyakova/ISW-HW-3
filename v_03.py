#!/usr/bin/env python3
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import librosa
import os
import time
from multiprocessing import Process
"""Take MFCC and put it in the catalog"""
NULL_PATH = "vox2_test_mp4"
def make_mfcc(new_path, our_folder):
    """Save as numpy array"""
    x, sr = librosa.load(new_path)
    mfcc = librosa.feature.mfcc(x, sr)
    np.save(our_folder, mfcc)
    
if __name__=='__main__':
    def check_folder(new_path, our_folder):
        """Looking for a 'mp4' file and build the catalog tree"""
        procs = []
        for filename in os.listdir(new_path):
            full_path_2 = os.path.join(new_path, filename)
            full_path_1 = os.path.join(our_folder, filename)
            if filename[filename.rfind("."):] == '.mp4':
                p = Process(target=make_mfcc, args=(full_path_2, full_path_1,))
                procs.append(p)
            else:
                os.makedirs(full_path_1)
                check_folder(full_path_2, full_path_1)
                continue
        for p in procs:
            p.start()
        for p in procs:
            p.join()
    start_time = time.time()
    answer_path = os.path.join(os.getcwd(), 'with_MFCC')
    os.mkdir(answer_path)
    check_folder(os.path.abspath(NULL_PATH), answer_path)
    print("Time: {}".format(time.time() - start_time))
