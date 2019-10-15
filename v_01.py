import numpy as np
import librosa
import os
import time
"""Take MFCC and put it in the catalog"""
NULL_PATH = "id00012"
def check_folder(new_path, our_folder):
    """Looking for a 'm4a' file and build the catalog tree"""
    for filename in os.listdir(new_path):
        if filename[filename.rfind(".") + 1:] == 'm4a':
            x, sr = librosa.load(new_path + '\\' + filename)
            mfcc = librosa.feature.mfcc(x, sr)
            np.save(our_folder + '\\' + filename[0:filename.rfind("."):], mfcc)
        else:
            os.makedirs(our_folder + '\\' + filename)
            check_folder(new_path + '\\' + filename, our_folder + '\\' + filename)
            continue
start_time = time.time()
#os.chdir('C:\\Users\\osbel\\Desktop')
answer_path = os.getcwd() + '\\with_MFCC'
os.mkdir(answer_path)
check_folder(os.path.abspath(NULL_PATH), answer_path)
print("Time: {}".format(time.time() - start_time))
