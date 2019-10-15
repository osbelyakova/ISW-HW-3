import numpy as np
import librosa
import os
import time
from threading import Thread
"""Take MFCC and put it in the catalog"""
NULL_PATH = "id00012"
def check_folder(new_path, our_folder):
    """Looking for a 'm4a' file and build the catalog tree"""
    threads = []
    for filename in os.listdir(new_path):
        if filename[filename.rfind(".") + 1:] == 'm4a':
            y, sr = librosa.load(new_path + '\\' + filename)
            mfcc = librosa.feature.mfcc(y, sr)
            np.save(our_folder + '\\' + filename[0:filename.rfind("."):], mfcc)
        else:
            os.makedirs(our_folder + '\\' + filename)
            t1 = Thread(target=check_folder, args=(new_path + '\\' + filename, our_folder + '\\' + filename,))
            threads.append(t1)
            continue
    for t1 in threads:
        t1.start()
    for t1 in threads:
        t1.join()
start_time = time.time()
#os.chdir('C:\\Users\\osbel\\Desktop')
answer_path = os.getcwd() + '\\with_MFCC'
os.mkdir(answer_path)
check_folder(os.path.abspath(NULL_PATH), answer_path)
print("Time: {}".format(time.time() - start_time))
