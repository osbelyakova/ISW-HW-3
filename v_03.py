import numpy as np
import librosa
import os
import time
from multiprocessing import Process
"""Take MFCC and put it in the catalog"""
NULL_PATH = "id05714"
def make_mfcc(new_path, our_folder):
    full_path = os.path.join(new_path, filename)
    x, sr = librosa.load(full_path)
    mfcc = librosa.feature.mfcc(x, sr)
    full_path = os.path.join(our_folder, filename[0:filename.rfind("."):])
    np.save(full_path, mfcc)   
    
if __name__=='__main__':
    def check_folder(new_path, our_folder):
        """Looking for a 'm4a' file and build the catalog tree"""
        procs = []
        for filename in os.listdir(new_path):
            if filename[filename.rfind(".") + 1:] == 'm4a':
                full_path = os.path.join(new_path, filename)
                x, sr = librosa.load(full_path)
                mfcc = librosa.feature.mfcc(x, sr)
                full_path = os.path.join(our_folder, filename[0:filename.rfind("."):])
                np.save(full_path, mfcc)
            else:
                full_path_1 = os.path.join(our_folder, filename)
                os.makedirs(full_path_1)
                full_path_2 = os.path.join(new_path, filename)
                p = Process(target=make_mfcc, args=(full_path_2, full_path_1,))
                procs.append(t1)
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
