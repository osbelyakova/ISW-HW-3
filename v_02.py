#!/usr/bin/env python3
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import librosa
import os
import time
from threading import Thread
"""Take MFCC and put it in the catalog"""
NULL_PATH = "vox2_test_mp4"
def make_mfcc(from_this, in_here):
    """Save as numpy array"""
    x, sr = librosa.load(from_this)
    mfcc = librosa.feature.mfcc(x, sr)
    np.save(in_here, mfcc)
if __name__ == '__main__':
    def check_folder(new_path, our_folder):
        """Looking for a 'mp4' file and build the catalog tree"""
        threads = []
        for filename in os.listdir(new_path):
            full_path_2 = os.path.join(new_path, filename)
            full_path_1 = os.path.join(our_folder, filename)
            if filename[filename.rfind("."):] == '.mp4':
                t = Thread(target=make_mfcc, args=(full_path_2, full_path_1,))
                threads.append(t)
            else:
                os.makedirs(full_path_1)
                check_folder(full_path_2, full_path_1)
                continue
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    start_time = time.time()
    answer_path = os.path.join(os.getcwd(), 'with_MFCC')
    os.mkdir(answer_path)
    check_folder(os.path.abspath(NULL_PATH), answer_path)
    print("Time: {}".format(time.time() - start_time))
